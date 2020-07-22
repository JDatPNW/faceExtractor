import tkinter
from tkinter import filedialog
from .Logger import Logger

class guiLogger(Logger):
    def __init__(self):
        self.mainLog = tkinter.Tk()
        self.mainLog.iconphoto(True, tkinter.PhotoImage(file="./src/imgs/icon.png"))
        self.mainLog.title('FaceExtractor Logger')
        self.vAutoScroll = tkinter.BooleanVar()
        self.vAutoScroll.set(True)
        self.scroll = tkinter.Scrollbar(self.mainLog)
        self.scroll.grid(row=2, column=4, sticky='ns')
        self.mainLogWindow()

    def end(self):
        self.mainLog.destroy()

    def mainLogWindow(self):
        tkinter.Label(self.mainLog, text="Face Extractor").grid(row=0, columnspan=3)

        self.lAutoScroll = tkinter.Label(self.mainLog, text = "Auto Scroll?")
        self.lAutoScroll.grid(row=1, column=0, sticky="W")

        self.rAutoScrollOn = tkinter.Radiobutton(self.mainLog, text="Yes", variable = self.vAutoScroll, value = True)
        self.rAutoScrollOn.grid(row=1, column=1, sticky="W")

        self.rAutoScrollOff = tkinter.Radiobutton(self.mainLog, text="No", variable = self.vAutoScroll, value = False)
        self.rAutoScrollOff.grid(row=1, column=2, sticky="W")

        self.tOutputField = tkinter.Text(self.mainLog, height=20, width=75,  wrap=tkinter.NONE, yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.tOutputField.yview)
        self.tOutputField.grid(row=2,columnspan=3)


    def logFaceCoordinates(self, i, d, scores, idx, visualize):
        self.printCoords =  "\tL...Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(i, d[0][0], d[0][1], d[1][0], d[1][1]) +"\n"
        self.printCoords= self.printCoords+ "\t\tL...score: {}, face_type:{}".format(round(scores[i],4), idx[i])+"\n"
        self.tOutputField.insert(tkinter.END, self.printCoords)
        self.mainLog.update_idletasks()
        self.mainLog.update()
        if(self.vAutoScroll.get()):
            self.tOutputField.yview_pickplace("end")

    def logNumFaces(self, dets, percentage, vidid, filelength):
        self.printNum = "Video " + str(vidid) + "/" + str(filelength) +  "| {:.2%} - "  "Number of faces detected this frame: {}".format(round((percentage), 4), len(dets)) +"\n"
        self.tOutputField.insert(tkinter.END, self.printNum)
        self.mainLog.update_idletasks()
        self.mainLog.update()
        if(self.vAutoScroll.get()):
            self.tOutputField.yview_pickplace("end")
