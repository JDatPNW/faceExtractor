from .Initializer import Initializer
import tkinter
from tkinter import filedialog


class guiInitializer(Initializer):

    def __init__(self):
        self.main = tkinter.Tk()
        self.main.title('FaceExtractor Config')
        self.main.iconphoto(True, tkinter.PhotoImage(
            file="./src/imgs/icon.png"))
        self.vTracker = tkinter.IntVar()
        self.vTracker.set(1)
        self.vVisual = tkinter.BooleanVar()
        self.vVisual.set(False)
        self.vLogger = tkinter.BooleanVar()
        self.vLogger.set(True)
        self.vVisualizer = tkinter.BooleanVar()
        self.vVisualizer.set(True)
        self.vArchiver = tkinter.IntVar()
        self.vArchiver.set(True)
        self.vLoader = tkinter.IntVar()
        self.vLoader.set(0)
        self.vThresh = tkinter.DoubleVar()
        self.vThresh.set(1.0)
        self.vSample = tkinter.DoubleVar()
        self.vSample.set(1.0)
        self.vOutputFolder = tkinter.StringVar()
        self.vOutputFolder.set("default")

    def end(self):
        self.main.destroy()

    def mainWindow(self):
        tkinter.Label(self.main, text="Face Extractor").grid(
            row=0, columnspan=3)

        self.lInputFile = tkinter.Label(
            self.main, text="Choose Input File: ").grid(row=1, column=0, sticky="W")
        self.bInputFile = tkinter.Button(
            self.main, text="Open", command=self.chooseInput)
        self.bInputFile.grid(row=1, column=1, sticky="W")

        self.lOutputFolder = tkinter.Label(
            self.main, text="Output Folder Name:").grid(row=2, column=0, sticky="W")
        self.eOutputFolder = tkinter.Entry(
            self.main, textvariable=self.vOutputFolder)
        self.eOutputFolder.grid(row=2, column=1, sticky="W")

        self.chooseTracker()
        self.chooseLogger()
        self.chooseLoader()
        self.chooseVisualize()
        self.chooseVisualizer()
        self.chooseArchiver()
        self.lThreshold = tkinter.Label(
            self.main, text="Threshold:").grid(row=3, column=0, sticky="W")
        self.sThreshold = tkinter.Scale(self.main, from_=0, to=10, resolution=0.1,
                                        variable=self.vThresh, length=250, tickinterval=1, orient="horizontal")
        self.sThreshold.grid(row=3, column=1, sticky="W")

        self.lSample = tkinter.Label(self.main, text="Sampling:").grid(
            row=4, column=0, sticky="W")
        self.sSample = tkinter.Scale(self.main, from_=0, to=10, resolution=0.1,
                                     variable=self.vSample, length=250, tickinterval=1, orient="horizontal")
        self.sSample.grid(row=4, column=1, sticky="W")

        self.bFinish = tkinter.Button(
            self.main, text="Start", command=self.end)
        self.bFinish.grid(row=11, columnspan=3)

    def chooseTracker(self):
        self.lTracker = tkinter.Label(self.main, text="Choose a Tracker:")
        self.lTracker.grid(row=5, column=0, sticky="W")

        self.rTrackerDLIB = tkinter.Radiobutton(
            self.main, text="dlib (Recommended)", variable=self.vTracker, value=1)
        self.rTrackerDLIB.grid(row=5, column=1, sticky="W")

        self.rTrackerOVC = tkinter.Radiobutton(
            self.main, text="OpenCV Haarecascade", variable=self.vTracker, value=0)
        self.rTrackerOVC.grid(row=5, column=2, sticky="W")

    def chooseLogger(self):
        self.lLogger = tkinter.Label(self.main, text="Choose a Logger:")
        self.lLogger.grid(row=6, column=0, sticky="W")

        self.rLoggerCL = tkinter.Radiobutton(
            self.main, text="Command Line (faster)", variable=self.vLogger, value=1)
        self.rLoggerCL.grid(row=6, column=1, sticky="W")

        self.rLoggerGUI = tkinter.Radiobutton(
            self.main, text="GUI", variable=self.vLogger, value=0)
        self.rLoggerGUI.grid(row=6, column=2, sticky="W")

    def chooseLoader(self):
        self.lLoader = tkinter.Label(
            self.main, text="What type of files do you want to load?:")
        self.lLoader.grid(row=7, column=0, sticky="W")

        self.rLoaderYT = tkinter.Radiobutton(
            self.main, text="YouTube Video", variable=self.vLoader, value=0)
        self.rLoaderYT.grid(row=7, column=1, sticky="W")

        self.rLoaderIMG = tkinter.Radiobutton(
            self.main, text="Images", variable=self.vLoader, value=1)
        self.rLoaderIMG.grid(row=7, column=2, sticky="W")

        self.rLoaderVID = tkinter.Radiobutton(
            self.main, text="Local Video", variable=self.vLoader, value=2)
        self.rLoaderVID.grid(row=7, column=3, sticky="W")

    def chooseArchiver(self):
        self.lArchiver = tkinter.Label(self.main, text="Choose how to safe the output:")
        self.lArchiver.grid(row=10, column=0, sticky="W")

        self.lArchiverJPG = tkinter.Radiobutton(
            self.main, text=".jpg", variable=self.vArchiver, value=1)
        self.lArchiverJPG.grid(row=10, column=1, sticky="W")

        self.lArchiverCSV = tkinter.Radiobutton(
            self.main, text=".csv", variable=self.vArchiver, value=0)
        self.lArchiverCSV.grid(row=10, column=2, sticky="W")

        self.lArchiverNP = tkinter.Radiobutton(
            self.main, text=".npy", variable=self.vArchiver, value=2)
        self.lArchiverNP.grid(row=10, column=3, sticky="W")

    def chooseVisualize(self):
        self.lVisual = tkinter.Label(self.main, text="Turn on the visualizer?")
        self.lVisual.grid(row=8, column=0, sticky="W")

        self.rVisualOn = tkinter.Radiobutton(
            self.main, text="Yes", variable=self.vVisual, value=True)
        self.rVisualOn.grid(row=8, column=1, sticky="W")

        self.rVisualOff = tkinter.Radiobutton(
            self.main, text="No (faster)", variable=self.vVisual, value=False)
        self.rVisualOff.grid(row=8, column=2, sticky="W")

    def chooseVisualizer(self):
        self.lVisualizer = tkinter.Label(
            self.main, text="Choose a Visualizer:")
        self.lVisualizer.grid(row=9, column=0, sticky="W")

        self.rVisualizerOCV = tkinter.Radiobutton(
            self.main, text="OpenCV (Faster)", variable=self.vVisualizer, value=1)
        self.rVisualizerOCV.grid(row=9, column=1, sticky="W")

        self.rVisualizerGUI = tkinter.Radiobutton(
            self.main, text="GUI", variable=self.vVisualizer, value=0)
        self.rVisualizerGUI.grid(row=9, column=2, sticky="W")

    def chooseInput(self):
        self.main.fInputFile = filedialog.askopenfilename(
            title="Select file", initialdir="./input/", filetypes=(("all files", "*.*"), (".txt files", "*.txt"), (".mp4 files", "*.mp4")))

    def getInput(self):
        self.mainWindow()
        self.main.mainloop()
        self.vOutputFolder_final = self.vOutputFolder.get() + "/"
        return (self.vVisual.get(), self.main.fInputFile, self.vOutputFolder_final,
                self.vThresh.get(), self.vSample.get(), self.vTracker.get(), self.vLogger.get(),
                self.vVisualizer.get(), self.vLoader.get(), self.vArchiver.get())
