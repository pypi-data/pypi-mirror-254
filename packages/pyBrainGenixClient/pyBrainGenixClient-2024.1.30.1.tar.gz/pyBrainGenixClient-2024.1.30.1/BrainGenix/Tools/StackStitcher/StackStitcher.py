# BrainGenix-NES
# AGPLv3

import os
import sys
import imageio

import PIL.Image
import PIL.ImageDraw



class SliceStitcher:

    def __init__(self, _Verbose:bool=False, _AddBorders:bool=False, _BorderSize_px:int=8, _LabelImages:bool=False, _MakeGif:bool=False):
        self.Verbose = _Verbose
        self.AddBorders = _AddBorders
        self.LabelImages = _LabelImages
        self.BorderSize_px = _BorderSize_px
        self.MakeGif = _MakeGif


    def GetNumberOfSlices(self, _FileList:list, _SimulationID:int, _RegionID:int):

        NumSlices:int = 0
        for File in _FileList:

            try:
                ParsedLine = File.replace(f"Simulation{_SimulationID}_Region{_RegionID}_Slice", "")
                SliceNumber = int(ParsedLine.split("_")[0])
                NumSlices = max(SliceNumber, NumSlices)
            except:
                pass

        # slice numbers start at 0, so we're adding +1 due to that
        return NumSlices + 1

    def GetSimulationIDs(self, _FileList:list):

        SimulationIDs:list = []
        for File in _FileList:
            ParsedLine = File.replace(f"Simulation", "")
            SimulationID = int(ParsedLine.split("_")[0])

            if not SimulationID in SimulationIDs:
                SimulationIDs.append(SimulationID)

        return SimulationIDs

    def GetRegionIDs(self, _FileList:list, _SimulationID:int):

        RegionIDs:list = []
        for File in _FileList:
            ParsedLine = File.replace(f"Simulation{_SimulationID}_Region", "")

            try:
                RegionID = int(ParsedLine.split("_")[0])
                if not RegionID in RegionIDs:
                    RegionIDs.append(RegionID)
            except:
                pass

        return RegionIDs

    def GetSimulationIDs(self, _FileList:list):

        NumSlimulations:int = 0
        for File in _FileList:
            ParsedLine = File.replace(f"Simulation", "")
            SliceNumber = int(ParsedLine.split("_")[0])
            NumSlimulations = max(SliceNumber, NumSlimulations)

        # Simulations start at 0, so we're adding +1 due to that
        return range(NumSlimulations + 1)

    def StitchSlice(self, _DirectoryPath:str, _OutputDir:str, _FileNames:list, _SimulationID:int, _RegionID:int):


        # Sort filenames to only include those with this sim and region
        SortedFiles = []
        for File in _FileNames:
            if f"Simulation{_SimulationID}_Region{_RegionID}" in File:
                SortedFiles.append(File)


        NumSlices = self.GetNumberOfSlices(_FileNames, _SimulationID, _RegionID)
        if (self.Verbose):
            print(f"    - Simulation {_SimulationID} Region {_RegionID} Has {NumSlices} Slice(s)")

        if not os.path.exists(_OutputDir):
            os.mkdir(_OutputDir)



        ReferenceImageSize = PIL.Image.open(_DirectoryPath + SortedFiles[0]).size

        # Lists to hold X and Y values
        Xvalues = []
        Yvalues = []
        for file_name in SortedFiles:
            File_NamexValue = file_name.find("_X")
            letter_at_position2 = (file_name[File_NamexValue+2])
            letter_at_position3 = (file_name[File_NamexValue+3])
            letter_at_position4 = (file_name[File_NamexValue+4])
            letter_at_position5 = (file_name[File_NamexValue+5])
            letter_at_position6 = (file_name[File_NamexValue+6])
            letter_at_position7 = (file_name[File_NamexValue+7])
            Xvalues.append(float(letter_at_position2+letter_at_position3+letter_at_position4+letter_at_position5+letter_at_position6+letter_at_position7))
        for file_name in SortedFiles:
            File_NamexValue = file_name.find("_Y")
            letter_at_position2 = (file_name[File_NamexValue+2])
            letter_at_position3 = (file_name[File_NamexValue+3])
            letter_at_position4 = (file_name[File_NamexValue+4])
            letter_at_position5 = (file_name[File_NamexValue+5])
            letter_at_position6 = (file_name[File_NamexValue+6])
            letter_at_position7 = (file_name[File_NamexValue+7])
            Yvalues.append(float(letter_at_position2+letter_at_position3+letter_at_position4+letter_at_position5+letter_at_position6+letter_at_position7))


        # Pair up the Xvalues and Y values into a list
        Yvalues = sorted(Yvalues)
        Xvalues = sorted(Xvalues)
        XList_Without_Duplicates = []
        YList_Without_Duplicates = []
        
        for item in Xvalues:
            if item not in XList_Without_Duplicates:
                XList_Without_Duplicates.append(item)
        for item in Yvalues:
            if item not in YList_Without_Duplicates:
                YList_Without_Duplicates.append(item)

        YIncrements = (YList_Without_Duplicates[1] - YList_Without_Duplicates[0])
        XIncrements = (XList_Without_Duplicates[1] - XList_Without_Duplicates[0])
        YTileCounter = len(YList_Without_Duplicates)
        XTileCounter = len(XList_Without_Duplicates)



        # Keep Track Of List Of Slice Images For Gif (If Enabled)
        SliceFilenames:list = []


        for ThisSliceNumber in range(NumSlices):

            OutputImageSize = [ReferenceImageSize[0] * XTileCounter, ReferenceImageSize[1] * YTileCounter]
            if (self.AddBorders):
                OutputImageSize[0] += self.BorderSize_px * (XTileCounter + 1)
                OutputImageSize[1] += self.BorderSize_px * (YTileCounter + 1)
            OutputSliceImage = PIL.Image.new("RGBA", OutputImageSize, (0, 255, 0, 255))

            for x in range(XTileCounter):
                for y in range(YTileCounter):
                    xposition = x * XIncrements
                    yposition = y * YIncrements

       

                    HasFoundImage = False
                    for XRoundingError in range(15):
                        for YRoundingError in range(15):

                            XPositionWithRoundingError = xposition + (XRoundingError * 0.000001)
                            YPositionWithRoundingError = yposition + (YRoundingError * 0.000001)

                            ypositionstring = "{:.{}f}".format(YPositionWithRoundingError, 6)
                            xpositionstring = "{:.{}f}".format(XPositionWithRoundingError, 6)

                            try:
                                TileImage = PIL.Image.open(_DirectoryPath + f"Simulation{_SimulationID}_Region{_RegionID}_Slice{ThisSliceNumber}_X" + xpositionstring + "_Y" + ypositionstring + ".png")
                                
                                # Optionally Label The Images Based On Position
                                if (self.LabelImages):

                                    Overlay = PIL.ImageDraw.Draw(TileImage)
                                    Overlay.text((16, 16), f"X{xpositionstring}um, Y{ypositionstring}um, Slice {ThisSliceNumber}", fill=(255, 0, 0))

                                
                                position = [x * ReferenceImageSize[0],  y * ReferenceImageSize[1]]  # Corrected positions

                                if (self.AddBorders):
                                            position[0] += ((x + 1) * self.BorderSize_px)
                                            position[1] += ((y + 1) * self.BorderSize_px)

                                OutputSliceImage.paste(TileImage, position)
                                HasFoundImage = True
                                break

                            except FileNotFoundError:
                                # print(f"Failed To Find Image: 'Simulation{_SimulationID}_Region{_RegionID}_Slice{ThisSliceNumber}_X" + xpositionstring + "_Y" + ypositionstring + ".png'")
                                pass

                        if (HasFoundImage):
                            break
                    
                    if (not HasFoundImage):
                        if (self.Verbose):
                            print(f"Error, could not find image for position {xposition}x, {yposition}y")
        
            # get slice number as a variable then use f string and i = i+1
            OutputImageFilename = f"{_OutputDir}/Simulation{_SimulationID}_Region{_RegionID}_Slice{ThisSliceNumber}.png"
            OutputSliceImage.save(OutputImageFilename)
            if (self.MakeGif):
                SliceFilenames.append(OutputImageFilename)

            if (self.Verbose):
                print(f"     - Stitched Simulation {_SimulationID} Region {_RegionID} Slice {ThisSliceNumber} ({XTileCounter}x{YTileCounter} images)")

        # Now, Create The Gif
        if (self.MakeGif):

            if (self.Verbose):
                print(f"    - Cresting Gif For Simulation {_SimulationID} Region {_RegionID}, This May Take A While")

            GifFilename:str = f"{_OutputDir}/Simulation{_SimulationID}_Region{_RegionID}.gif"
            with imageio.get_writer(GifFilename, mode='I', loop=0) as Writer:
                for Filename in SliceFilenames:
                    Image = imageio.v3.imread(Filename)
                    ImageNoAlpha = Image[:,:,:3]
                    Writer.append_data(ImageNoAlpha)


            if (self.Verbose):
                print(f"    - Created Gif For Simulation {_SimulationID} Region {_RegionID}")



def StackStitcher(_InputDirectory:str, _OutputDirectory:str="OutDir", _AddBorders:bool=True, _LabelImages:bool=True, _BorderSize_px:int=8, _MakeGif:bool=True, _Verbose=True):

    # Ensure Paths Ends With /
    if not _InputDirectory.endswith("/"):
        _InputDirectory += "/"

    # Setup Slice Stitcher
    SS:SliceStitcher = SliceStitcher(_Verbose, _AddBorders, _BorderSize_px, _LabelImages, _MakeGif)

    # Reconstruct
    Images = os.listdir(_InputDirectory)
    SimulationIDs = SS.GetSimulationIDs(Images)
    if (_Verbose):
        print(f"Detected {len(SimulationIDs)} Simulation(s) To Stitch")
    for SimID in SimulationIDs:
        if (_Verbose):
            print(f" - Stitching Simulation With ID {SimID}")

        Regions = SS.GetRegionIDs(Images, SimID)
        if (_Verbose):
            print(f" - Detected {len(Regions)} Region(s) In Simulation")

        for RegionID in Regions:
            if (_Verbose):
                print(f"  - Stitching Region {RegionID}")
            SS.StitchSlice(_InputDirectory, _OutputDirectory, Images, SimID, RegionID)


