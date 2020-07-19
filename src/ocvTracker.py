import cv2
from .Tracker import Tracker

class ocvTracker(Tracker):
    def __init__(self):
        pass

    def initTracker(self):
        self.detector = cv2.CascadeClassifier('./src/haarcascades/haarcascade_frontalface_alt.xml')


    def detectFaces(self, frame, sampling, threshold):
        self.coords = ()
        self.coordsList = []
        self.scores = []
        self.idx= []
        self.gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        self.dets = self.detector.detectMultiScale(self.gray, float(sampling), int(threshold))
        for (x, y, w, h) in self.dets:
            self.coords = ((x, y), (x+w, y+h))
            self.coordsList.append(self.coords)
            self.scores.append(0)
            self.idx.append(0)
        return self.coordsList, self.scores, self.idx
