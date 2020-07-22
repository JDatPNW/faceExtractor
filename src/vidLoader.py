import cv2
from .Loader import Loader


class vidLoader(Loader):

    def loadList(self, inputfile):
        list = []
        list.append(inputfile)
        return list

    def loadStream(self, url):
        cap = cv2.VideoCapture(url)
        return cap, url

    def getFileLength(self, file):
        for i, l in enumerate(file):
            pass
        return i + 1
