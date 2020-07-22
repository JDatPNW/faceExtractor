import numpy
import cv2
import PIL
from PIL import ImageTk, Image
import tkinter
import cv2
from .Visualizer import Visualizer


class guiVisualizer(Visualizer):

    def __init__(self, vis, log):
        self.visualize = vis
        self.window = log
        self.first = True
        self.panel = tkinter.Label()
        self.basewidth = 400
        self.skip = False

    def setupWindow(self):
        pass

    def displayVideo(self, frame):
        if(self.visualize == 1):
            tempimg = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            tempimg = PIL.Image.fromarray(tempimg)
            wpercent = (self.basewidth / float(tempimg.size[0]))
            hsize = int((float(tempimg.size[1]) * float(wpercent)))
            tempimg = tempimg.resize((self.basewidth, hsize))
            img = ImageTk.PhotoImage(tempimg)
            if self.first:
                self.panel = tkinter.Label(self.window.mainLog, image=img)
                self.panel.grid(row=3, columnspan=3)
                self.first = False
                self.bFinish = tkinter.Button(
                    self.window.mainLog, text="Skip Current Video", command=self.end)
                self.bFinish.grid(row=4, columnspan=3)
            self.panel.configure(image=img)
            self.panel.image = img
            self.window.mainLog.update_idletasks()
            self.window.mainLog.update()
            if self.skip:
                self.skip = False
                return 1
            else:
                return 0

    def end(self):
        self.skip = True

    def highlightFaces(self, frame, d):
        if(self.visualize == 1):
            cv2.rectangle(frame, (d[0][0], d[0][1]),
                          (d[1][0], d[1][1]), (255, 0, 0), 2)

    def closeWindows(self):
        pass
