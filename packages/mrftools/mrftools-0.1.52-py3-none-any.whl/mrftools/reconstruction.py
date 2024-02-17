import ismrmrd
import numpy as np
import torch 
from torch import fft as FFT
from mrftools import SequenceParameters, DictionaryParameters, Simulation, SequenceType
import time
import torchkbnufft as tkbn
from tqdm import tqdm
from mrftools import DictionaryEntry, coilCombination
import kornia as K
import nibabel as nib
import fbpca

def LoadB1DataFromNIFTI(niftiFilepath, b1Range=(0.5, 1.55), b1Stepsize=0.10, b1IdentityValue=800):
    b1 = np.flip(nib.load(niftiFilepath).get_fdata(), axis=2) # Why is this flip needed?
    b1Bins = np.arange(b1Range[0], b1Range[1], b1Stepsize)
    b1Clipped = np.clip(b1, np.min(b1Bins)*b1IdentityValue, np.max(b1Bins)*b1IdentityValue)
    b1Binned = b1Bins[np.digitize(b1Clipped, b1Bins*b1IdentityValue, right=True)]
    return b1Binned

def LoadSpirals(trajectoryFilepath, densityFilepath, numSpirals=48):
    trajectoryBuffer = np.fromfile(trajectoryFilepath, dtype=np.complex64)
    trajectories = np.split(trajectoryBuffer, numSpirals)
    densityBuffer = np.fromfile(densityFilepath, dtype=np.float32)
    densities = np.split(densityBuffer, numSpirals)
    print("Found", np.shape(trajectories), "spirals")
    return (trajectoryBuffer, trajectories, densityBuffer, densities)

def CalculateVoxelOffsetAcquisitionSpace(header, acqHeader, matrixSizeOverride=None):
    mm_offset_acquisition_space = np.zeros((3))
    mm_offset_acquisition_space[0] = (acqHeader.position[0]*acqHeader.read_dir[0])+(acqHeader.position[1]*acqHeader.read_dir[1])+(acqHeader.position[2]*acqHeader.read_dir[2]);
    mm_offset_acquisition_space[1] = (acqHeader.position[0]*acqHeader.phase_dir[0])+(acqHeader.position[1]*acqHeader.phase_dir[1])+(acqHeader.position[2]*acqHeader.phase_dir[2]);
    mm_offset_acquisition_space[2] = (acqHeader.position[0]*acqHeader.slice_dir[0])+(acqHeader.position[1]*acqHeader.slice_dir[1])+(acqHeader.position[2]*acqHeader.slice_dir[2]);
    voxel_size = np.zeros((3)) 
    if matrixSizeOverride is None:
        voxel_size[0] = header.encoding[0].reconSpace.fieldOfView_mm.x/header.encoding[0].reconSpace.matrixSize.x
        voxel_size[1] = header.encoding[0].reconSpace.fieldOfView_mm.y/header.encoding[0].reconSpace.matrixSize.y
        voxel_size[2] = header.encoding[0].reconSpace.fieldOfView_mm.z/header.encoding[0].reconSpace.matrixSize.z
    else:
        voxel_size[0] = float(header.encoding[0].reconSpace.fieldOfView_mm.x)/float(matrixSizeOverride[0])
        voxel_size[1] = float(header.encoding[0].reconSpace.fieldOfView_mm.y)/float(matrixSizeOverride[1])
        voxel_size[2] = float(header.encoding[0].reconSpace.fieldOfView_mm.z)/float(matrixSizeOverride[2])
    voxel_offset_acquisition_space = mm_offset_acquisition_space/voxel_size
    return voxel_offset_acquisition_space

def ApplyXYZShiftKSpace(svdData, header, acqHeaders, trajectories, matrixSizeOverride=None):
    shape = np.shape(svdData)
    numSVDComponents=shape[0]; numCoils=shape[1]; numPartitions=shape[2]; numReadoutPoints=shape[3]; numSpirals=shape[4]
    shiftedSvdData = torch.zeros_like(svdData)
    # For now, assume all spirals/partitions/etc have same offsets applied
    (x_shift, y_shift, z_shift) = CalculateVoxelOffsetAcquisitionSpace(header, acqHeaders[0,0,0], matrixSizeOverride=matrixSizeOverride)
    trajectories = torch.t(torch.tensor(np.array(trajectories)))
    x = torch.zeros((numPartitions, numReadoutPoints, numSpirals));
    y = torch.zeros((numPartitions, numReadoutPoints, numSpirals));
    partitions = torch.moveaxis(torch.arange(0.5, -0.5, -1/numPartitions).expand((numReadoutPoints, numSpirals, numPartitions)), -1,0)
    trajectories = trajectories.expand((numPartitions, numReadoutPoints, numSpirals))
    x = torch.cos(-2*torch.pi*(x_shift*trajectories.real + y_shift*trajectories.imag + z_shift*partitions));
    y = torch.sin(-2*torch.pi*(x_shift*trajectories.real + y_shift*trajectories.imag + z_shift*partitions));
    print("K-Space x/y/z shift applied:", x_shift, y_shift, z_shift)
    return svdData*torch.complex(x,y)

def ApplyZShiftImageSpace(imageData, header, acqHeaders, matrixSizeOverride=None):
    (x_shift, y_shift, z_shift) = CalculateVoxelOffsetAcquisitionSpace(header, acqHeaders[0,0,0], matrixSizeOverride=matrixSizeOverride)
    return torch.roll(imageData, int(z_shift), dims=2)

def rSVD(A, Omega, numPowerIterations=1, full_matrices=False):
    Y = torch.matmul(A,Omega)
    for q in range(numPowerIterations):
        Y = torch.matmul(A ,torch.matmul(torch.t(A), Y))
    Q, _ = torch.linalg.qr(Y)
    B = torch.matmul(torch.t(Q), A)
    u_tilde, s, v = torch.linalg.svd(B, full_matrices=full_matrices)
    u = torch.matmul(Q, u_tilde)
    return u, s, v

# modes
# None: normal pytorch SVD
# "randomized": rSVD implementation above
# "fbpca": facebook's randomized PCA/SVD 
def CalculateSVD(simulation, truncationNumber, mode=None, numPowerIterations=1, seed=2147483647):
    dictionary = torch.t(torch.tensor(simulation.results))
    dictionaryNorm = torch.sqrt(torch.sum(torch.pow(torch.abs(dictionary[:,:]),2),1))
    dictionaryShape = np.shape(dictionary)
    normalizedDictionary = torch.zeros_like(dictionary)
    for i in range(dictionaryShape[0]):
        normalizedDictionary[i,:] = dictionary[i,:]/dictionaryNorm[i]
    if(mode=="randomized"):
        randGen = torch.Generator(); randGen.manual_seed(seed)
        omega = torch.randn(dictionary.shape[1], truncationNumber, generator=randGen, dtype=torch.complex128)
        (u,s,v) = rSVD(normalizedDictionary, omega, numPowerIterations=numPowerIterations, full_matrices=False)
    if(mode=="fbpca"):
        (u,s,v) = fbpca.pca(normalizedDictionary.numpy(), k=truncationNumber, n_iter=numPowerIterations, raw=False)
        s = torch.tensor(s) 
        v = torch.tensor(v)
    if(mode=="lowrank"):
        (u,s,v) = torch.svd_lowrank(normalizedDictionary, q=truncationNumber, niter=numPowerIterations)
    else:      
        (u,s,v) = torch.linalg.svd(normalizedDictionary, full_matrices=False)
    vt = torch.t(v)
    truncationMatrix = vt[:,0:truncationNumber]
    truncatedResults = torch.t(torch.matmul(normalizedDictionary,truncationMatrix))
    singularValues = s
    return truncationMatrix, truncatedResults, singularValues[0:truncationNumber]

# Raw Data should have shape [coil, partitions, readouts, spirals, spiralTimepoints]
def ApplySVDCompression(rawdata, simulation, device=None):
    if(device==None):
        if torch.cuda.is_available():
            device = torch.device("cuda")
        else:
            device = torch.device("cpu")
    sizes = np.shape(rawdata)
    numCoils=sizes[0]; numPartitions=sizes[1]; numReadoutPoints=sizes[2]; numSpirals=sizes[3]; numTimepointsPerSpiralArm=sizes[4]
    numSVDComponents=np.shape(simulation.truncationMatrix)[1]
    svdData = torch.zeros((numSVDComponents, numCoils, numPartitions, numReadoutPoints, numSpirals), dtype=torch.complex64)
    with tqdm(total=numSpirals) as pbar:
        for spiral in np.arange(0,numSpirals):
            truncationMatrix = torch.zeros((numTimepointsPerSpiralArm, numSVDComponents), dtype=torch.complex64).to(device)
            for spiralTimepoint in np.arange(0,numTimepointsPerSpiralArm):
                realTimepoint = numSpirals*spiralTimepoint + spiral
                truncationMatrix[spiralTimepoint, :] = torch.tensor(simulation.truncationMatrix[realTimepoint, :])
            raw = torch.tensor(rawdata[:,:,:,spiral, :], dtype=torch.complex64).to(device)
            result = torch.matmul(raw, truncationMatrix)
            svdData[:,:, :, :, spiral] = torch.moveaxis(result, -1, 0)
            pbar.update(1)
            del raw, truncationMatrix
    torch.cuda.empty_cache()
    print("SVD Compressed Raw Data Shape:", np.shape(svdData))   
    return svdData

# SVD Data should have shape [svdComponents, coils, partitions, readouts, spirals]
def PerformNUFFTs(svdData, trajectoryBuffer, densityBuffer, matrixSize, gridSize,device=None):
    if(device==None):
        if torch.cuda.is_available():
            device = torch.device("cuda")
        else:
            device = torch.device("cpu")
    sizes = np.shape(svdData)
    numSVDComponents=sizes[0]; numCoils=sizes[1]; numPartitions=sizes[2]; numReadoutPoints=sizes[3]; numSpirals=sizes[4]
    trajectorySplit = np.stack((trajectoryBuffer.real, trajectoryBuffer.imag))*2*np.pi
    ktraj_device = torch.tensor(trajectorySplit, dtype=torch.float32).to(device)
    densityBuffer_device = torch.tensor(densityBuffer).to(device)
    nufft_device = tkbn.KbNufftAdjoint(im_size=tuple(matrixSize[0:2]), grid_size=tuple(gridSize[0:2]),).to(device)
    t = time.time()

    nufftResults = torch.zeros((numSVDComponents, numCoils, numPartitions, matrixSize[0], matrixSize[1]), dtype=torch.complex64)
    with tqdm(total=numPartitions) as pbar:
        for partition in np.arange(0,numPartitions):
            readout_device = torch.swapaxes(svdData[:, :, partition, :, :], -1,-2).reshape(numSVDComponents, numCoils, -1).to(device)
            nufftResult = nufft_device(readout_device * densityBuffer_device, ktraj_device)
            nufftResults[:,:,partition,:,:] = nufftResult
            del readout_device, nufftResult
            pbar.update(1)
    del ktraj_device, densityBuffer_device, nufft_device
    torch.cuda.empty_cache()
    print("Nufft Results Shape:", np.shape(nufftResults))   
    return nufftResults

def PerformThroughplaneFFT(nufftResults, device=None):
    if(device==None):
        if torch.cuda.is_available():
            device = torch.device("cuda")
        else:
            device = torch.device("cpu")
    sizes = np.shape(nufftResults)
    numSVDComponents=sizes[0]; numCoils=sizes[1]; numPartitions=sizes[2]; matrixSize=sizes[3:5]
    images = torch.zeros((numSVDComponents, numCoils, numPartitions, matrixSize[0], matrixSize[1]), dtype=torch.complex64)
    with tqdm(total=numSVDComponents) as pbar:
        for svdComponent in np.arange(0, numSVDComponents):
            images[svdComponent,:,:,:,:] = torch.fft.ifftshift(torch.fft.ifft(nufftResults[svdComponent,:,:,:,:], dim=1), dim=1)
            pbar.update(1)
    torch.cuda.empty_cache()
    print("Images Shape:", np.shape(images))   
    return images
    
# Images should have shape [svdComponents, coils, z, x, y]
def PerformSumOfSquaresCoilCombination(images, takeAbsolute=False):
    if(takeAbsolute):
        images = torch.abs(images)
    combined = torch.square(images)
    combined = torch.sum(combined, axis=1)
    combined = torch.sqrt(combined)
    combined = torch.moveaxis(combined, 1,-1)
    print("Coil-Combined Images Shape:", np.shape(combined))
    return combined

# Images should have shape [svdComponents, coils, z, x, y]
def PerformWalshCoilCombination(images, verbose=False, kernelSize=(5,5,1), niter=5, device=None):
    if(device==None):
        if torch.cuda.is_available():
            device = torch.device("cuda")
        else:
            device = torch.device("cpu")
    t = time.time()
    shape = np.shape(images)
    combinedImageData = torch.zeros((shape[0], shape[2], shape[3], shape[4]), dtype=torch.complex64)
    coil_map, rho = coilCombination.calculateCoilmapsWalsh(images[0,:,:,:,:], smoothing=kernelSize, niter=niter) 
    with tqdm(total=shape[0]) as pbar:
        for svdComponent in np.arange(0,shape[0]):
            im = (images[svdComponent, :, :, :, :]).to(device)
            combinedImageData[svdComponent, :, :, :] = torch.sum((im * torch.conj(coil_map)), axis=0)
            del im
            pbar.update(1)

    torch.cuda.empty_cache()
    print("Coil Combination Complete in", time.time()-t, "seconds")
    return torch.moveaxis(combinedImageData, 1,-1), coil_map

# Images should have shape [svdComponents, coils, z, x, y]
def PerformInatiCoilCombination(images, verbose=False, kernelSize=5, niter=5, device=None):
    if(device==None):
        if torch.cuda.is_available():
            device = torch.device("cuda")
        else:
            device = torch.device("cpu")
    t = time.time()
    shape = np.shape(images)
    combinedImageData = torch.zeros((shape[0], shape[2], shape[3], shape[4]), dtype=torch.complex64)
    coil_map, combinedImageData[0, :, :, :] = coilCombination.calculateCoilmapsInati(images[0,:,:,:,:], verbose=verbose, smoothing=kernelSize, niter=niter) 
    for svdComponent in np.arange(1,shape[0]):
        im = (images[svdComponent, :, :, :, :]).to(device)
        combinedImageData[svdComponent, :, :, :] = torch.sum((im * torch.conj(coil_map)), axis=0)
        del im
    torch.cuda.empty_cache()
    print("Coil Combination Complete in", time.time()-t, "seconds")
    return torch.moveaxis(combinedImageData, 1,-1), coil_map

def GenerateMaskFromCoilmaps(coilmaps, thresholdType='mean', thresholdValue=0.0001, applyClosing=False, closingKernelSize=10, applyOpening=False, openingKernelSize=10, applyFeathering=False, featheringKernelSize=3, device=None):
    if(device==None):
        if torch.cuda.is_available():
            device = torch.device("cuda")
        else:
            device = torch.device("cpu")
    with torch.no_grad():
        coilmapSum = torch.sum(torch.abs(coilmaps),0)
        coilmapSumsPerPartition = coilmapSum.flatten(1,-1)
        if thresholdType == 'mean':
            threshold = torch.mean(coilmapSumsPerPartition,1).unsqueeze(1).unsqueeze(1) * thresholdValue
        if thresholdType == 'quantile':
            threshold = torch.quantile(coilmapSumsPerPartition, 1, thresholdValue).unsqueeze(1).unsqueeze(1)
        mask = coilmapSum > threshold
        if applyClosing:
            Y, X = np.ogrid[:closingKernelSize, :closingKernelSize]
            dist_from_center = np.sqrt((X - closingKernelSize/2)**2 + (Y-closingKernelSize/2)**2)
            closingKernel = torch.tensor(dist_from_center <= closingKernelSize/2).to(torch.float32).to(device)  
            mask = K.morphology.closing(mask.unsqueeze(0).to(torch.float32), closingKernel).squeeze()
            del Y, X, dist_from_center, closingKernel
        if applyOpening:
            Y, X = np.ogrid[:openingKernelSize, :openingKernelSize]
            dist_from_center = np.sqrt((X - openingKernelSize/2)**2 + (Y-openingKernelSize/2)**2)
            openingKernel = torch.tensor(dist_from_center <= openingKernelSize/2).to(torch.float32).to(device)  
            mask = K.morphology.opening(mask.unsqueeze(0), openingKernel).squeeze()
            del Y, X, dist_from_center, openingKernel
        if applyFeathering:
            meanFilter = torch.nn.Conv3d(in_channels=1, out_channels=1, kernel_size=featheringKernelSize, bias=False, padding='same')
            featheringKernelWeights = (torch.ones((featheringKernelSize, featheringKernelSize, featheringKernelSize), 
                                                  dtype=torch.float32)/(featheringKernelSize*featheringKernelSize*featheringKernelSize)).to(device)
            meanFilter.weight.data = featheringKernelWeights.unsqueeze(0).unsqueeze(0)
            mask = meanFilter(mask.unsqueeze(0)).squeeze()
            del featheringKernelWeights, meanFilter
    outputMask = torch.moveaxis(mask, 0,-1).cpu()
    del coilmapSum, coilmapSumsPerPartition, threshold, mask
    torch.cuda.empty_cache()
    return outputMask


def BatchedPatternMatchViaMaxInnerProduct(signalTimecourses, dictionaryEntries, dictionaryEntryTimecourses, voxelsPerBatch=500, device=None):
    if(device==None):
        if torch.cuda.is_available():
            device = torch.device("cuda")
        else:
            device = torch.device("cpu")

    signalsTransposed = torch.t(signalTimecourses)
    signalNorm = torch.linalg.norm(signalsTransposed, axis=1)[:,None]
    normalizedSignals = signalsTransposed / signalNorm

    simulationResults = torch.tensor(dictionaryEntryTimecourses, dtype=torch.complex64)
    simulationNorm = torch.linalg.norm(simulationResults, axis=0)
    normalizedSimulationResults = torch.t((simulationResults / simulationNorm)).to(device)

    numBatches = int(np.shape(normalizedSignals)[0]/voxelsPerBatch)
    patternMatches = np.empty((np.shape(normalizedSignals)[0]), dtype=DictionaryEntry)
    M0 = torch.zeros(np.shape(normalizedSignals)[0], dtype=torch.complex64)
    with tqdm(total=numBatches) as pbar:
        for i in range(numBatches):
            firstVoxel = i*voxelsPerBatch
            if i == (numBatches-1):
                lastVoxel = np.shape(normalizedSignals)[0]
            else:
                lastVoxel = firstVoxel+voxelsPerBatch
            batchSignals = normalizedSignals[firstVoxel:lastVoxel,:].to(device)
            innerProducts = torch.inner(batchSignals, normalizedSimulationResults)
            maxInnerProductIndices = torch.argmax(torch.abs(innerProducts), 1, keepdim=True)
            maxInnerProducts = torch.take_along_dim(innerProducts,maxInnerProductIndices,dim=1).squeeze()
            signalNorm_device = signalNorm[firstVoxel:lastVoxel].squeeze().to(device)
            simulationNorm_device = simulationNorm.to(device)[maxInnerProductIndices.squeeze().to(torch.long)]
            M0_device = signalNorm_device/simulationNorm_device
            M0[firstVoxel:lastVoxel] = M0_device.cpu()
            patternMatches[firstVoxel:lastVoxel] = dictionaryEntries[maxInnerProductIndices.squeeze().to(torch.long).cpu()].squeeze()
            pbar.update(1)
            del batchSignals, M0_device, signalNorm_device, simulationNorm_device
    del normalizedSimulationResults, dictionaryEntryTimecourses, dictionaryEntries, signalsTransposed, signalNorm, normalizedSignals, simulationResults
    del simulationNorm
    return patternMatches, M0

def PerformPatternMatchingViaMaxInnerProduct(combined, dictionary, simulation, voxelsPerBatch=500, b1Binned=None, device=None,):
    if(device==None):
        if torch.cuda.is_available():
            device = torch.device("cuda")
        else:
            device = torch.device("cpu")
    sizes = np.shape(combined)
    numSVDComponents=sizes[0]; matrixSize=sizes[1:4]
    patternMatches = np.empty((matrixSize), dtype=DictionaryEntry)
    M0 = torch.zeros((matrixSize), dtype=torch.complex64)
    if b1Binned is not None:
        for uniqueB1 in np.unique(b1Binned):
            print(uniqueB1)
            if uniqueB1 == 0:
                patternMatches[b1Binned==uniqueB1] = 0
            else:
                signalTimecourses = combined[:,b1Binned == uniqueB1]
                simulationTimecourses = torch.t(torch.t(torch.tensor(simulation.truncatedResults))[(np.argwhere(dictionary.entries['B1'] == uniqueB1))].squeeze())
                dictionaryEntries = dictionary.entries[(np.argwhere(dictionary.entries['B1'] == uniqueB1))]
                signalTimecourses = combined[:,b1Binned == uniqueB1]
                patternMatches[b1Binned == uniqueB1], M0[b1Binned == uniqueB1] = BatchedPatternMatchViaMaxInnerProduct(signalTimecourses,dictionaryEntries,simulationTimecourses,voxelsPerBatch, device=device)
    else:
        signalTimecourses = torch.reshape(combined, (numSVDComponents,-1))
        if(dictionary.entries['B1'][0]):
            simulationTimecourses = torch.t(torch.t(torch.tensor(simulation.truncatedResults))[(np.argwhere(dictionary.entries['B1'] == 1))].squeeze())
            dictionaryEntries = dictionary.entries[(np.argwhere(dictionary.entries['B1'] == 1))]
        else:   
            simulationTimecourses = torch.tensor(simulation.truncatedResults)
            dictionaryEntries = dictionary.entries
        patternMatches, M0 = BatchedPatternMatchViaMaxInnerProduct(signalTimecourses, dictionaryEntries, simulationTimecourses, voxelsPerBatch, device=device)
    patternMatches = np.reshape(patternMatches, (matrixSize))
    M0 = np.reshape(M0, (matrixSize)).numpy()
    M0 = np.nan_to_num(M0)
    return patternMatches, M0