import dlib
from .Tracker import Tracker


class dlibTracker(Tracker):
    def __init__(self):
        pass

    def initTracker(self):
        self.detector = dlib.get_frontal_face_detector()

    def detectFaces(self, frame, sampling, threshold):
        self.coords = ()
        self.coordsList = []
        self.dets, self.scores, self.idx = self.detector.run(
            frame, int(sampling), float(threshold))
        for i, d in enumerate(self.dets):
            self.coords = ((d.left(), d.top()), (d.right(), d.bottom()))
            self.coordsList.append(self.coords)
        return self.coordsList, self.scores, self.idx
