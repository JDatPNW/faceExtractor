import cv2
import numpy
import os
from .Tracker import Tracker
from src.cnn.dmnet import dmnet


class jdTracker(Tracker):
    def __init__(self):
        self.WIDTH = 160
        self.HEIGHT = 90
        self.LR = 1e-3
        self.MODEL_NAME = os.path.dirname(os.path.abspath(
            __file__)) + '/cnn/JD-dmnet-FaceX.model'

    def initTracker(self):
        self.model = dmnet(self.WIDTH, self.HEIGHT, self.LR)
        self.model.load(self.MODEL_NAME)

    def detectFaces(self, frame, sampling, threshold):
        frame = numpy.array(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        height, width = frame.shape
        height = height / self.HEIGHT
        width = width / self.WIDTH
        frame = cv2.resize(frame, (self.WIDTH, self.HEIGHT))
        self.coords = ()
        self.coordsList = []
        self.scores = []
        self.idx = []
        self.prediction = self.model.predict([frame.reshape(self.WIDTH, self.HEIGHT, 1)])[0]
        print(self.prediction)
        self.scores.append(0)
        self.idx.append(0)
        self.coords = (
            [int(self.prediction[0]*width), int(self.prediction[1]*height)], [int(self.prediction[2]*width), int(self.prediction[3]*height)])
        self.coordsList.append(self.coords)
        return self.coordsList, self.scores, self.idx
