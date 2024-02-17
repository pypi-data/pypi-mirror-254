import numpy as np
import h5py
from matplotlib import pyplot as plt
import torch
from tqdm import tqdm

from mrftools import DictionaryParameters, SequenceParameters

class Simulation: 
    def __init__(self,sequenceParameters, dictionaryParameters, name="", numTimepoints = -1, phaseRange=(-2*np.pi, 2*np.pi), numSpins=1, results=[], truncationMatrix=[], truncatedResults=[], singularValues=[], initialMz=-0.95):
        self.sequenceParameters = sequenceParameters
        self.dictionaryParameters = dictionaryParameters
        if numTimepoints == -1:
            numTimepoints = len(sequenceParameters.timepoints)
        self.numTimepoints = numTimepoints
        self.phaseRange = phaseRange
        self.numSpins = numSpins
        self.results = results
        self.truncationMatrix = truncationMatrix
        self.truncatedResults = truncatedResults
        self.singularValues = singularValues
        self.initialMz = initialMz
        if not name:
            self.name = sequenceParameters.name + "_" + dictionaryParameters.name + "_" + str(numSpins) # Doesn't account for phase range
        else:
            self.name = name

    @staticmethod
    def Simulate(numTimepoints,T1s,T2s,B1s,TRs,TEs,FAs,spinOffresonances,device=None, initialMz=-0.95, delay=-1, applyInversion=True):     
        if(device==None):
            if torch.cuda.is_available():
                device = torch.device("cuda")
            else:
                device = torch.device("cpu")    

        T1s = torch.tensor(T1s).to(device)
        T2s = torch.tensor(T2s).to(device)
        B1s = torch.tensor(B1s).to(device)
        FAs = torch.tensor(FAs).to(device)
        spinOffresonances = torch.tensor(spinOffresonances).to(device)
        Mx0 = torch.zeros((numTimepoints,len(spinOffresonances),len(T1s)))
        My0 = torch.zeros((numTimepoints,len(spinOffresonances),len(T1s)))
        Mz0 = torch.zeros((numTimepoints,len(spinOffresonances),len(T1s)))
        Mx = torch.zeros((len(spinOffresonances),len(T1s))).to(device) # No initial x magnetization
        My = torch.zeros((len(spinOffresonances),len(T1s))).to(device) # No initial y magnetization
        Mz = torch.ones((len(spinOffresonances),len(T1s))).to(device)  # No initial z magnetization

        FAs = torch.deg2rad(FAs)
        phaseValueCosines = torch.cos(spinOffresonances)
        phaseValueSines = torch.sin(spinOffresonances)
        
        runIndex = 0
        if delay > 0:
            At2delay = torch.exp(-1*delay/T2s)
            At1delay = torch.exp(-1*delay/T1s)
            Bt1delay = 1-At1delay
            runIndex = -1

        with torch.no_grad():
            while runIndex < 1:
                Mx[:] = Mx[:] *  0.00 # Clear all x magnetization
                My[:] = Mx[:] *  0.00 # Clear all y magnetization
                if(applyInversion):
                    Mz[:] = Mz[:] * -0.95 # Apply inversion with 95% efficiency
                for iTimepoint in range(numTimepoints):
                    fa = FAs[iTimepoint] * B1s
                    tr = TRs[iTimepoint]
                    te = TEs[iTimepoint]
                    tre = tr-te
                    
                    At2te = torch.exp(-1*te/T2s)
                    At1te = torch.exp(-1*te/T1s)
                    Bt1te = 1-At1te
                    
                    At2tr = torch.exp(-1*tre/T2s)
                    At1tr = torch.exp(-1*tre/T1s)
                    Bt1tr = 1-At1tr
                
                    crf = torch.cos(fa)
                    srf = torch.sin(fa)

                    # Applying flip angle 
                    Myi = My
                    Mzi = Mz
                    My = torch.multiply(crf,Myi)-torch.multiply(srf,Mzi)
                    Mz = torch.multiply(srf,Myi)+torch.multiply(crf,Mzi)

                    # Relaxation over TE
                    Mx = torch.multiply(Mx, At2te)
                    My = torch.multiply(My, At2te)
                    Mz = torch.multiply(Mz, At1te)+Bt1te

                    # Reading value after TE and before TRE 
                    Mx0[iTimepoint,:,:]=Mx.cpu()
                    My0[iTimepoint,:,:]=My.cpu()
                    Mz0[iTimepoint,:,:]=Mz.cpu()

                    # Relaxation over TRE (TR-TE) 
                    Mx = Mx*At2tr
                    My = My*At2tr
                    Mz = Mz*At1tr+Bt1tr

                    # Applying off-resonance to spins
                    Mxi = Mx.t()
                    Myi = My.t()
                    Mx = (torch.multiply(phaseValueCosines,Mxi) - torch.multiply(phaseValueSines,Myi)).t()
                    My = (torch.multiply(phaseValueSines,Mxi) + torch.multiply(phaseValueCosines,Myi)).t()
                    del fa, tr, te, tre, At2te, At1te, Bt1te, At2tr, At1tr, Bt1tr, crf, srf, Mxi, Myi, Mzi 
                    
                if delay > 0:
                    # Relaxation over delay time
                    Mx = torch.multiply(Mx, At2delay)
                    My = torch.multiply(My, At2delay)
                    Mz = torch.multiply(Mz, At1delay)+Bt1delay
                runIndex += 1

        del T1s, T2s, B1s, FAs, spinOffresonances, Mx, My, Mz
        return Mx0,My0,Mz0

    def Execute(self, numBatches=1, device=None):
        if(device==None):
            if torch.cuda.is_available():
                device = torch.device("cuda")
            else:
                device = torch.device("cpu")
        TRs = np.copy(self.sequenceParameters.timepoints['TR'])
        TEs = np.copy(self.sequenceParameters.timepoints['TE'])
        FAs = np.copy(self.sequenceParameters.timepoints['FA'])
        phaseValues = np.linspace(self.phaseRange[0], self.phaseRange[1], self.numSpins)
        dictEntriesPerBatch = int(len(self.dictionaryParameters.entries)/numBatches)
        print("Simulating " + str(numBatches) + " batch(s) of ~" + str(dictEntriesPerBatch) + " dictionary entries")
        Mxy = np.zeros((self.numTimepoints, len(self.dictionaryParameters.entries)), np.complex128)
        with tqdm(total=numBatches) as pbar:
            for i in range(numBatches):
                firstDictEntry = i*dictEntriesPerBatch
                if i == (numBatches-1):
                    lastDictEntry = len(self.dictionaryParameters.entries)
                else:
                    lastDictEntry = firstDictEntry+dictEntriesPerBatch
                T1s = np.copy(self.dictionaryParameters.entries[firstDictEntry:lastDictEntry]['T1'])
                T2s = np.copy(self.dictionaryParameters.entries[firstDictEntry:lastDictEntry]['T2'])
                B1s = np.copy(self.dictionaryParameters.entries[firstDictEntry:lastDictEntry]['B1'])
                Mx0,My0,Mz0 = self.Simulate(self.numTimepoints, T1s, T2s, B1s, TRs, TEs, FAs, phaseValues, device=device, initialMz=self.initialMz, delay=self.sequenceParameters.delay, applyInversion=self.sequenceParameters.applyInversion)
                Mx = torch.mean(Mx0, axis=1)    
                My = torch.mean(My0, axis=1)    
                Mxy[:,firstDictEntry:lastDictEntry] = Mx+(My*1j)
                pbar.update(1)
            self.results = Mxy
        return self.results

    def CalculateSVD(self, desiredSVDPower=0.99, truncationNumberOverride=None):
        dictionary = self.results.transpose()
        dictionaryNorm = np.sqrt(np.sum(np.power(np.abs(dictionary[:,:]),2),1))
        dictionaryShape = np.shape(dictionary)
        normalizedDictionary = np.zeros_like(dictionary)
        for i in range(dictionaryShape[0]):
            normalizedDictionary[i,:] = dictionary[i,:]/dictionaryNorm[i]
        (u,s,v) = np.linalg.svd(normalizedDictionary, full_matrices=False)
        self.singularValues = s
        if truncationNumberOverride == None:
            (truncationNumber, totalSVDPower) = self.GetTruncationNumberFromDesiredPower(desiredSVDPower)
        else:
            truncationNumber = truncationNumberOverride
            totalSVDPower = self.GetPowerFromDesiredTruncationNumber(truncationNumber)
        vt = np.transpose(v)
        self.truncationMatrix = vt[:,0:truncationNumber]
        self.truncatedResults = np.matmul(normalizedDictionary,self.truncationMatrix).transpose()
        return (truncationNumber, totalSVDPower)

    def GetTruncationNumberFromDesiredPower(self, desiredSVDPower):
        singularVectorPowers = self.singularValues/np.sum(self.singularValues)
        totalSVDPower=0; numSVDComponents=0
        for singularVectorPower in singularVectorPowers:
            totalSVDPower += singularVectorPower
            numSVDComponents += 1
            if totalSVDPower > desiredSVDPower:
                break
        return numSVDComponents, totalSVDPower

    def GetPowerFromDesiredTruncationNumber(self, desiredTruncationNumber):
        singularVectorPowers = self.singularValues/np.sum(self.singularValues)
        totalSVDPower=np.sum(singularVectorPowers[0:desiredTruncationNumber])
        return totalSVDPower

    def Export(self, filename, force=False, includeFullResults=True, includeSVDResults=True):
        if ".mrf" in filename:
            outfile = h5py.File(filename, "a")
            try:
                outfile.create_group("simulations")
            except:
                pass
            if (self.name in list(outfile["simulations"].keys())) and not force:
                print("Simulation '" + self.name + "' already exists in .mrf file. Specify 'force' to overwrite")
            else:
                try:
                    del outfile["simulations"][self.name]
                except:
                    pass
                simulation = outfile["simulations"].create_group(self.name)
                simulation.attrs.create("name", self.name)
                simulation.attrs.create("numTimepoints", self.numTimepoints)
                simulation.attrs.create("phaseRange", self.phaseRange)
                simulation.attrs.create("numSpins", self.numSpins)
                self.sequenceParameters.Export(filename, force)
                simulation["sequenceParameters"] = outfile["/sequenceParameters/"+self.sequenceParameters.name]
                self.dictionaryParameters.Export(filename, force)
                simulation["dictionaryParameters"] = outfile["/dictionaryParameters/"+self.dictionaryParameters.name]
                if(includeFullResults):
                    simulation["results"] = self.results
                else:
                    simulation["results"] = []
                if(includeFullResults):
                    simulation["truncationMatrix"] = self.truncationMatrix
                    simulation["truncatedResults"] = self.truncatedResults
                else:
                    simulation["truncationMatrix"] = []
                    simulation["truncatedResults"] = []

                outfile.close()
        else:
            print("Input is not a .mrf file")

    def Plot(self, numTimepoints=-1, dictionaryEntryNumbers=[], plotTruncated=False):
        if numTimepoints == -1:
            numTimepoints = len(self.sequenceParameters.timepoints)
        if dictionaryEntryNumbers == []:
            dictionaryEntryNumbers = [int(len(self.dictionaryParameters.entries)/2)]
        ax = plt.subplot(1,1,1)
        if not plotTruncated:
            for entry in dictionaryEntryNumbers:
                plt.plot(abs(self.results[:,entry]), label=str(self.dictionaryParameters.entries[entry]))
        else:
            for entry in dictionaryEntryNumbers:
                plt.plot(abs(self.truncatedResults[:,entry]), label=str(self.dictionaryParameters.entries[entry]))
        ax.legend()

    def GetAverageResult(self, indices):
        return np.average(self.results[:,indices], 1)

    def FindPatternMatches(self, querySignals, useSVD=False, truncationNumber=25):
        if querySignals.ndim == 1:
            querySignals = querySignals[:,None]
        if not useSVD:
            querySignalsTransposed = querySignals.transpose()
            normalizedQuerySignal = querySignalsTransposed / np.linalg.norm(querySignalsTransposed, axis=1)[:,None]
            simulationResultsTransposed = self.results.transpose()
            normalizedSimulationResultsTransposed = simulationResultsTransposed / np.linalg.norm(simulationResultsTransposed, axis=1)[:,None]
            innerProducts = np.inner(normalizedQuerySignal, normalizedSimulationResultsTransposed)
            return np.argmax(abs(innerProducts), axis=1)
        else:
            if self.truncatedResults[:] == []:
                self.CalculateSVD(truncationNumber)
            signalsTransposed = querySignals.transpose()
            signalSVDs = np.matmul(signalsTransposed, self.truncationMatrix)
            normalizedQuerySignalSVDs = signalSVDs / np.linalg.norm(signalSVDs, axis=1)[:,None]
            simulationResultsTransposed = self.truncatedResults.transpose()
            normalizedSimulationResultsTransposed = simulationResultsTransposed / np.linalg.norm(simulationResultsTransposed, axis=1)[:,None]
            innerProducts = np.inner(normalizedQuerySignalSVDs, normalizedSimulationResultsTransposed)
            return np.argmax(abs(innerProducts), axis=1)

    @staticmethod
    def Import(filename, simulationName):
        if ".mrf" in filename:
            infile = h5py.File(filename, "r")
            simulationGroup = infile["simulations"][simulationName]
            simulationName = simulationGroup.attrs.get("name")
            simulationNumTimepoints = simulationGroup.attrs.get("numTimepoints")
            simulationPhaseRange = simulationGroup.attrs.get("phaseRange")
            simulationNumSpins = simulationGroup.attrs.get("numSpins")
            simulationResults = simulationGroup["results"][:]
            simulationTruncationMatrix = simulationGroup["truncationMatrix"][:]
            simulationTruncatedResults = simulationGroup["truncatedResults"][:]
            sequenceParametersGroup = simulationGroup["sequenceParameters"]
            importedSequenceParameters = SequenceParameters(sequenceParametersGroup.attrs.get("name"), sequenceParametersGroup["timepoints"][:])
            dictionaryParametersGroup = simulationGroup["dictionaryParameters"]
            importedDictionaryParameters = DictionaryParameters(dictionaryParametersGroup.attrs.get("name"), dictionaryParametersGroup["entries"][:])
            new_simulation = Simulation(importedSequenceParameters, importedDictionaryParameters, simulationName, simulationNumTimepoints, simulationPhaseRange, simulationNumSpins, simulationResults, simulationTruncationMatrix, simulationTruncatedResults)
            infile.close()
            return new_simulation
        else:
            print("Input is not a .mrf file")
    
    @staticmethod
    def GetAvailableSimulations(filename):
        if ".mrf" in filename:
            infile = h5py.File(filename, "r")
            return list(infile["simulations"].keys())
        else:
            print("Input is not a .mrf file")

