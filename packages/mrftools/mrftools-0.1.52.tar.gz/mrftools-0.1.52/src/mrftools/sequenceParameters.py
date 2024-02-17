from __future__ import annotations
import numpy as np
import h5py
from mrftools import SequenceType, Units
from matplotlib import pyplot as plt


Timepoint = np.dtype([('TR', np.float32), ('TE', np.float32), ('FA', np.float32), ('PH', np.float32), ('ID', np.int16)])

class SequenceParameters:
    def __init__(self, name:str, type:SequenceType, timepoints=[], delay=-1.0, applyInversion=True):
        self.name = name
        self.type = type
        self.timepoints = timepoints
        self.delay = delay
        self.applyInversion = applyInversion

    def __str__(self):
        return self.name + " || Type: " + self.type + " || " + str(self.timepoints)

    def Initialize(self, TRs:list(float), TEs:list(float), FAs:list(float), PHs:list(float), IDs:list(int)):
        self.timepoints = np.empty(len(TRs), dtype=Timepoint)
        if (len(TRs)!=len(TEs)) or (len(TRs)!=len(FAs)) or  (len(TRs)!=len(PHs)) or  (len(TRs)!=len(IDs)):
            print("Sequence Parameter Import Failed: TR/TE/FA/PH/ID files must have identical number of entries")
            return 
        for index in range(len(TRs)):
            self.timepoints[index] = (TRs[index], TEs[index], FAs[index], PHs[index], IDs[index])
        print("Sequence Parameter set '"+ self.name + "' initialized with " + str(len(self.timepoints)) + " timepoint definitions")
   
    def Export(self, filename:str, force=False):
        if ".mrf" in filename:
            outfile = h5py.File(filename, "a")
            try:
                outfile.create_group("sequenceParameters")
            except:
                pass
            if (self.name in list(outfile["sequenceParameters"].keys())) and not force:
                print("Sequence Parameter set '" + self.name + "' already exists in .mrf file. Specify 'force' to overwrite")
            else:
                try:
                    del outfile["sequenceParameters"][self.name]
                except:
                    pass
                sequenceParameters = outfile["sequenceParameters"].create_group(self.name)
                sequenceParameters.attrs.create("name", self.name)
                sequenceParameters.attrs.create("type", self.type.name)
                sequenceParameters["timepoints"] = self.timepoints
                outfile.close()
        else:
            print("Input is not a .mrf file")

    def ExportToTxt(self, baseFilepath="", timeUnits=Units.MICROSECONDS, angleUnits=Units.DEGREES, exportIntegers=True):
        sequenceFile = open(baseFilepath+self.name+".txt","w")
        scaledTimepoints = np.copy(self.timepoints)
        scaledTimepoints['TR'] = self.__convertUnits(self.timepoints['TR'], Units.SECONDS, timeUnits)
        scaledTimepoints['TE'] = self.__convertUnits(self.timepoints['TE'], Units.SECONDS, timeUnits)
        scaledTimepoints['FA'] = self.__convertUnits(self.timepoints['FA'], Units.DEGREES, angleUnits)
        scaledTimepoints['PH'] = self.__convertUnits(self.timepoints['PH'], Units.DEGREES, angleUnits)
        if(exportIntegers):
            scaledTimepoints = scaledTimepoints.astype(np.dtype([('TR', np.int16), ('TE', np.int16), ('FA', np.int16), ('PH', np.int16), ('ID', np.int16)]))
        print(timeUnits.name, file=sequenceFile)
        print(angleUnits.name, file=sequenceFile)
        print(self.type.name, file=sequenceFile)
        print("TR | TE | FA | PH | ID", file=sequenceFile)
        for timepoint in scaledTimepoints:
            print(timepoint["TR"], timepoint["TE"], timepoint["FA"], timepoint["PH"], timepoint["ID"], file=sequenceFile)
        sequenceFile.close()

    def ExportToSeparateTxt(self, baseFilepath="", timeUnits=Units.MICROSECONDS, angleUnits=Units.DEGREES, exportIntegers=True):
        print("WARNING: Separate Txt File Support is a legacy feature, and should NOT be used for new sequence devlopment.")
        scaledTimepoints = np.copy(self.timepoints)
        scaledTimepoints['TR'] = self.__convertUnits(self.timepoints['TR'], Units.SECONDS, timeUnits)
        scaledTimepoints['TE'] = self.__convertUnits(self.timepoints['TE'], Units.SECONDS, timeUnits)
        scaledTimepoints['FA'] = self.__convertUnits(self.timepoints['FA'], Units.DEGREES, angleUnits)
        scaledTimepoints['PH'] = self.__convertUnits(self.timepoints['PH'], Units.DEGREES, angleUnits)
        if(exportIntegers):
            scaledTimepoints = scaledTimepoints.astype(np.dtype([('TR', np.int16), ('TE', np.int16), ('FA', np.int16), ('PH', np.int16), ('ID', np.int16)]))
        trFile = open(baseFilepath+self.name+"_TRs.txt","w")
        teFile = open(baseFilepath+self.name+"_TEs.txt","w")
        faFile = open(baseFilepath+self.name+"_FAs.txt","w")
        phFile = open(baseFilepath+self.name+"_PHs.txt","w")
        idFile = open(baseFilepath+self.name+"_IDs.txt","w")
        for timepoint in scaledTimepoints:
            trFile.write(f'{timepoint["TR"]:7.5f}'+"\n")
            teFile.write(f'{timepoint["TE"]:7.5f}'+"\n") 
            faFile.write(f'{timepoint["FA"]:7.5f}'+"\n")   
            phFile.write(f'{timepoint["PH"]:7.5f}'+"\n")   
            idFile.write(f'{timepoint["ID"]:7.5f}'+"\n")   
        trFile.close()
        teFile.close()
        faFile.close()
        phFile.close()
        idFile.close()
        
    def Plot(self, numTimepoints=-1, figsize=(15,10), dpi=60):
        if numTimepoints == -1:
            numTimepoints = len(self.timepoints)
        plt.figure(figsize=figsize, dpi=dpi)
        plt.subplot(511)
        plt.plot(range(numTimepoints), self.timepoints['TR'][0:numTimepoints])
        plt.gca().set_title("TRs")
        plt.subplot(512)
        plt.plot(range(numTimepoints), self.timepoints['TE'][0:numTimepoints])
        plt.gca().set_title("TEs")
        plt.subplot(513)
        plt.plot(range(numTimepoints), self.timepoints['FA'][0:numTimepoints])
        plt.gca().set_title("FAs")
        plt.subplot(514)
        plt.plot(range(numTimepoints), self.timepoints['PH'][0:numTimepoints])
        plt.gca().set_title("PHs")        
        plt.subplot(515)
        plt.plot(range(numTimepoints), self.timepoints['ID'][0:numTimepoints])
        plt.gca().set_title("IDs")

    @staticmethod
    def GetAvailableSequenceParameters(filename:str) -> list(str):
        if ".mrf" in filename:
            infile = h5py.File(filename, "r")
            return list(infile["sequenceParameters"].keys())
        else:
            print("Input is not a .mrf file")

    @staticmethod
    def Import(filename:str, name:str) -> SequenceParameters:
        if ".mrf" in filename:
            infile = h5py.File(filename, "r")
            sequenceParameterGroup = infile["sequenceParameters"][name]
            sequenceParameterName = sequenceParameterGroup.attrs.get("name")
            sequenceParameterType = sequenceParameterGroup.attrs.get("type")
            new_sequence = SequenceParameters(sequenceParameterName, sequenceParameterType, sequenceParameterGroup["timepoints"][:])
            infile.close()
            return new_sequence
        else:
            print("Input is not a .mrf file")

    @staticmethod
    def ImportFromTxt(name:str, filepath:str) -> SequenceParameters:
        file = open(filepath, 'r')
        lines = file.read().splitlines()
        timeUnits = Units[lines[0]]
        angleUnits = Units[lines[1]]
        sequenceType = SequenceType[lines[2]]
        TRs=[]; TEs=[]; FAs=[]; PHs=[]; IDs=[]
        for lineNumber in np.arange(4, len(lines)):
            vals = lines[lineNumber].split()
            TRs.append(float(vals[0]))
            TEs.append(float(vals[1]))
            FAs.append(float(vals[2]))
            PHs.append(float(vals[3]))
            IDs.append(int(vals[4]))
        TRs = SequenceParameters.__convertUnits(np.array(TRs), timeUnits, Units.SECONDS)
        TEs = SequenceParameters.__convertUnits(np.array(TEs), timeUnits, Units.SECONDS)
        FAs = SequenceParameters.__convertUnits(np.array(FAs), angleUnits, Units.DEGREES)
        PHs = SequenceParameters.__convertUnits(np.array(PHs), angleUnits, Units.DEGREES)
        new_sequence_parameters = SequenceParameters(name, sequenceType)
        new_sequence_parameters.Initialize(TRs, TEs, FAs, PHs, IDs)
        file.close()
        return new_sequence_parameters

    @staticmethod
    def ImportFromSeparateTxt(name:str, type:SequenceType, trFilepath:str, teFilepath:str, faFilepath:str, phFilepath:str, idFilepath:str, baseTR = 0) -> SequenceParameters:
        new_sequence_parameters = SequenceParameters(name, type)
        TRs = SequenceParameters.__convertUnits(np.loadtxt(trFilepath), Units.MICROSECONDS, Units.SECONDS)
        TRs = TRs + baseTR
        TEs = SequenceParameters.__convertUnits(np.loadtxt(teFilepath), Units.MICROSECONDS, Units.SECONDS)
        FAs = np.loadtxt(faFilepath)
        PHs = np.loadtxt(phFilepath)
        IDs = np.loadtxt(idFilepath)
        new_sequence_parameters.Initialize(TRs, TEs, FAs, PHs, IDs)
        return new_sequence_parameters

    @staticmethod
    def __convertUnits(input, inputUnits, outputUnits):
        if(inputUnits == Units.SECONDS):
            if(outputUnits == Units.SECONDS):
                return input
            if(outputUnits == Units.MILLISECONDS):
                return input*1000
            if(outputUnits == Units.MICROSECONDS):
                return input*(1000*1000)
            else:
                print("Cannot convert", inputUnits, "to", outputUnits)
                return None
        if(inputUnits == Units.MILLISECONDS):
            if(outputUnits == Units.SECONDS):
                return input/1000
            if(outputUnits == Units.MILLISECONDS):
                return input
            if(outputUnits == Units.MICROSECONDS):
                return input*1000
            else:
                print("Cannot convert", inputUnits, "to", outputUnits)
                return None
        if(inputUnits == Units.MICROSECONDS):
            if(outputUnits == Units.SECONDS):
                return input/(1000*1000)
            if(outputUnits == Units.MILLISECONDS):
                return input/1000
            if(outputUnits == Units.MICROSECONDS):
                return input
            else:
                print("Cannot convert", inputUnits, "to", outputUnits)
                return None
        if(inputUnits == Units.DEGREES):
            if(outputUnits == Units.DEGREES):
                return input
            if(outputUnits == Units.RADIANS):
                return (input/180)*np.pi
            else:
                print("Cannot convert", inputUnits, "to", outputUnits)
                return None
        if(inputUnits == Units.RADIANS):
            if(outputUnits == Units.DEGREES):
                return (input/np.pi)*180
            if(outputUnits == Units.RADIANS):
                return input
            else:
                print("Cannot convert", inputUnits, "to", outputUnits)
                return None
        else:
            print("Cannot convert", inputUnits, "to", outputUnits)
            return None 