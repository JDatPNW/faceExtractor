from .Initializer import Initializer
import tkinter
from tkinter import filedialog


class guiInitializer(Initializer):

    def __init__(self):
        self.main = tkinter.Tk()
        self.main.title('FaceExtractor Config')
        self.main.iconphoto(True, tkinter.PhotoImage(file="./src/imgs/icon.png"))
        self.vTracker = tkinter.IntVar()
        self.vTracker.set(1)
        self.vVisual = tkinter.BooleanVar()
        self.vVisual.set(False)
        self.vThresh = tkinter.DoubleVar()
        self.vThresh.set(1.0)
        self.vSample = tkinter.DoubleVar()
        self.vSample.set(1.0)
        self.vOutputFolder = tkinter.StringVar()
        self.vOutputFolder.set("default")

    def end(self):
        self.main.destroy()

    def mainWindow(self):
        tkinter.Label(self.main, text="Face Extractor").grid(row=0, columnspan=3)

        self.lInputFile = tkinter.Label(self.main, text = "Choose Input File: ").grid(row=1, column=0, sticky="W")
        self.bInputFile = tkinter.Button(self.main, text = "Open", command = self.chooseInput)
        self.bInputFile.grid(row=1, column=1, sticky="W")

        self.lOutputFolder = tkinter.Label(self.main, text = "Output Folder Name:").grid(row=2, column=0, sticky="W")
        self.eOutputFolder = tkinter.Entry(self.main, textvariable=self.vOutputFolder)
        self.eOutputFolder.grid(row=2, column=1, sticky="W")

        self.chooseTracker()
        self.chooseVisualize()

        self.lThreshold = tkinter.Label(self.main, text = "Threshold:").grid(row=3, column=0, sticky="W")
        self.sThreshold = tkinter.Scale(self.main, from_=0, to=10, resolution=0.1, variable = self.vThresh, length=250 ,tickinterval=1, orient="horizontal")
        self.sThreshold.grid(row=3, column=1, sticky="W")

        self.lSample = tkinter.Label(self.main, text = "Sampling:").grid(row=4, column=0, sticky="W")
        self.sSample = tkinter.Scale(self.main, from_=0, to=10, resolution=0.1, variable = self.vSample, length=250 ,tickinterval=1, orient="horizontal")
        self.sSample.grid(row=4, column=1, sticky="W")

        self.bFinish = tkinter.Button(self.main, text = "Start", command = self.end)
        self.bFinish.grid(row=7, columnspan=3)


    def chooseTracker(self):
        self.lTracker = tkinter.Label(self.main, text = "Choose a Tracker:")
        self.lTracker.grid(row=5, column=0, sticky="W")

        self.rTrackerDLIB = tkinter.Radiobutton(self.main, text="dlib (Recommended)", variable = self.vTracker, value = 1)
        self.rTrackerDLIB.grid(row=5, column=1, sticky="W")

        self.rTrackerOVC = tkinter.Radiobutton(self.main, text="OpenCV Haarecascade", variable = self.vTracker, value = 0)
        self.rTrackerOVC.grid(row=5, column=2, sticky="W")

    def chooseVisualize(self):
        self.lVisual = tkinter.Label(self.main, text = "Turn on the visualizer?")
        self.lVisual.grid(row=6, column=0, sticky="W")

        self.rVisualOn = tkinter.Radiobutton(self.main, text="Yes", variable = self.vVisual, value = True)
        self.rVisualOn.grid(row=6, column=1, sticky="W")

        self.rVisualOff = tkinter.Radiobutton(self.main, text="No", variable = self.vVisual, value = False)
        self.rVisualOff.grid(row=6, column=2, sticky="W")

    def chooseInput(self):
        self.chooseDir = tkinter.Tk()
        self.main.fInputFile = filedialog.askopenfilename(title = "Select file", initialdir = "./input/", filetypes = ((".txt files","*.txt"),("all files","*.*")))
        self.chooseDir.destroy()

    def getInput(self):
        self.mainWindow()
        self.main.mainloop()
        self.vOutputFolder_final = self.vOutputFolder.get() + "/"
        return self.vVisual.get(), self.main.fInputFile, self.vOutputFolder_final, self.vThresh.get(), self.vSample.get(), self.vTracker.get()
