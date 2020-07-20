from .Initializer import Initializer
import tkinter
from tkinter import filedialog


class guiInitializer(Initializer):

    def __init__(self):
        self.main = tkinter.Tk()
        self.main.title('FaceExtractor Config')
        self.tracker = tkinter.StringVar()
        self.tracker.set("dlib")
        self.visual = tkinter.BooleanVar()
        self.visual.set(False)
        self.thresh = tkinter.DoubleVar()
        self.thresh.set(1.0)
        self.samp = tkinter.DoubleVar()
        self.samp.set(1.0)
        self.folder = tkinter.StringVar()
        self.folder.set("default")

    def end(self):
        self.main.destroy()

    def mainWindow(self):
        tkinter.Label(self.main, text="Face Extractor").grid(row=0, columnspan=3)

        self.indirLabel = tkinter.Label(self.main, text = "Choose Input File: ").grid(row=1, column=0, sticky="W")
        self.indir = tkinter.Button(self.main, text = "Open", command = self.chooseInput)
        self.indir.grid(row=1, column=1, sticky="W")

        self.folderLabel = tkinter.Label(self.main, text = "Output Folder Name:").grid(row=2, column=0, sticky="W")
        self.folderinput = tkinter.Entry(self.main, textvariable=self.folder)
        self.folderinput.grid(row=2, column=1, sticky="W")

        self.chooseTracker()
        self.chooseVisualize()

        self.threshholdLabel = tkinter.Label(self.main, text = "Threshold:").grid(row=3, column=0, sticky="W")
        self.threshold = tkinter.Scale(self.main, from_=0, to=10, resolution=0.1, variable = self.thresh, length=250 ,tickinterval=1, orient="horizontal")
        self.threshold.grid(row=3, column=1, sticky="W")

        self.samplingLabel = tkinter.Label(self.main, text = "Sampling:").grid(row=4, column=0, sticky="W")
        self.sampling = tkinter.Scale(self.main, from_=0, to=10, resolution=0.1, variable = self.samp, length=250 ,tickinterval=1, orient="horizontal")
        self.sampling.grid(row=4, column=1, sticky="W")

        self.fini = tkinter.Button(self.main, text = "Start", command = self.end)
        self.fini.grid(row=7, columnspan=3)


    def chooseTracker(self):
        self.trackerChoice = tkinter.Label(self.main, text = "Choose a Tracker:")
        self.trackerChoice.grid(row=5, column=0, sticky="W")

        self.trackerDLIB = tkinter.Radiobutton(self.main, text="dlib (Recommended)", variable = self.tracker, value = "dlib")
        self.trackerDLIB.grid(row=5, column=1, sticky="W")

        self.trackerOCV = tkinter.Radiobutton(self.main, text="OpenCV Haarecascade", variable = self.tracker, value = "ocv")
        self.trackerOCV.grid(row=5, column=2, sticky="W")

    def chooseVisualize(self):
        self.visualChoice = tkinter.Label(self.main, text = "Turn on the visualizer?")
        self.visualChoice.grid(row=6, column=0, sticky="W")

        self.visualOn = tkinter.Radiobutton(self.main, text="Yes", variable = self.visual, value = True)
        self.visualOn.grid(row=6, column=1, sticky="W")

        self.visualOff = tkinter.Radiobutton(self.main, text="No", variable = self.visual, value = False)
        self.visualOff.grid(row=6, column=2, sticky="W")

    def chooseInput(self):
        self.chooseDir = tkinter.Tk()
        self.main.inputdir = filedialog.askopenfilename(title = "Select file", initialdir = "./input/", filetypes = ((".txt files","*.txt"),("all files","*.*")))
        self.chooseDir.destroy()

    def getInput(self):
        self.mainWindow()
        self.main.mainloop()

        return self.visual.get(), self.main.inputdir, self.folder.get(), self.thresh.get(), self.samp.get()
