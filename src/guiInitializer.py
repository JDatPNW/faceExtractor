from .Initializer import Initializer
import tkinter
from tkinter import filedialog


class guiInitializer(Initializer):

    def __init__(self):
        self.main = tkinter.Tk()
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
        self.indir = tkinter.Button(self.main, text = "Choose Input File", command = self.chooseInput)
        self.indir.pack()

        self.folderinput = tkinter.Entry(self.main, textvariable=self.folder)
        self.folderinput.pack()

        self.chooseTracker()
        self.chooseVisualize()

        self.threshold = tkinter.Scale(self.main, from_=0, to=10, resolution=0.1, variable = self.thresh, length=250 ,tickinterval=0.1, orient="horizontal")
        self.threshold.pack()

        self.sampling = tkinter.Scale(self.main, from_=0, to=10, resolution=0.1, variable = self.samp, length=250 ,tickinterval=0.1, orient="horizontal")
        self.sampling.pack()

        self.fini = tkinter.Button(self.main, text = "Start", command = self.end)
        self.fini.pack()


    def chooseTracker(self):
        self.trackerChoice = tkinter.Label(self.main, text = "Choose a Tracker:")
        self.trackerChoice.pack()

        self.trackerDLIB = tkinter.Radiobutton(self.main, text="dlib (Recommended)", variable = self.tracker, value = "dlib")
        self.trackerDLIB.pack(side="left")

        self.trackerOCV = tkinter.Radiobutton(self.main, text="OpenCV Haarecascade", variable = self.tracker, value = "ocv")
        self.trackerOCV.pack(side="left")

    def chooseVisualize(self):
        self.visualChoice = tkinter.Label(self.main, text = "Do you want to turn on the visualizer?")
        self.visualChoice.pack()

        self.visualOn = tkinter.Radiobutton(self.main, text="Yes", variable = self.visual, value = True)
        self.visualOn.pack(side="left")

        self.visualOff = tkinter.Radiobutton(self.main, text="No", variable = self.visual, value = False)
        self.visualOff.pack(side="left")

    def chooseInput(self):
        self.chooseDir = tkinter.Tk()
        self.main.inputdir = filedialog.askopenfilename(title = "Select file", initialdir = "./input/", filetypes = ((".txt files","*.txt"),("all files","*.*")))
        self.chooseDir.destroy()

    def chooseOutput(self):
        self.chooseDir = tkinter.Tk()
        self.main.outputdir = filedialog.askdirectory()
        self.chooseDir.destroy()

    def getInput(self):
        self.mainWindow()
        self.main.mainloop()

        return self.visual.get(), self.main.inputdir, self.folder.get(), self.thresh.get(), self.samp.get()
