import cv2
import pafy
from .Loader import Loader


class ytLoader(Loader):

    def loadList(self, inputfile):
        file = open(inputfile, "r")
        return file

    def loadStream(self, url):
        video = pafy.new(url)
        best = video.getbest(preftype="mp4")
        cap = cv2.VideoCapture()
        return cap, best.url

    def getFileLength(self, file):
        for i, l in enumerate(file):
            pass
        return i + 1
