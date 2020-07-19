import cv2, pafy, os

class Loader:

    def loadList(self, inputfile):
        inputlocation = "./input/" + inputfile
        file = open(inputlocation, "r")
        return file

    def loadStream(self, url):
        video = pafy.new(url)
        best = video.getbest(preftype="mp4")
        cap = cv2.VideoCapture()
        return cap, best

    def getFileLength(self, file):
        for i, l in enumerate(file):
            pass
        return i+1
