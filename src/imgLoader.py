import cv2
import os
from PIL import Image
import glob
import shutil
from .Loader import Loader


class imgLoader(Loader):

    def loadList(self, inputfile):
        dir = inputfile
        if os.path.isfile(inputfile):
            dir = os.path.dirname(inputfile)
            print(dir)
        list = []
        list.append(dir)
        return list

    def getFileLength(self, file):
        for i, l in enumerate(file):
            pass
        return i + 1

    def getFileName(self, currentImage):
        digits = len(str(currentImage))
        prefix = ""
        for i in range(5 - digits):
            prefix = prefix + "0"
        name = prefix + str(currentImage)
        return name

    def PNGtoJPG(self, dir):
        for file in list(glob.glob(dir + '*.png')):
            png = Image.open(file)
            png = png.convert("RGB")
            png.save(file + ".jpg")
            os.remove(file)

    def makeVid(self, newdir):
        cap = cv2.VideoCapture()
        images = str(newdir) + "%05d.jpg"
        return images, cap

    def loadStream(self, dir):
        newdir = dir + "_new/"
        dir = dir + "/"
        self.PNGtoJPG(dir)
        if not os.path.exists(newdir):
            os.makedirs(newdir)
        for count, filename in enumerate(os.listdir(dir)):
            newName = self.getFileName(count + 1)
            dst = newName + ".jpg"
            src = dir + filename
            dst = newdir + dst
            shutil.copyfile(src, dst)
        images, cap = self.makeVid(newdir)
        return cap, images
