import cv2
import re
import os
import numpy
from .Archiver import Archiver


class npArchiver(Archiver):

    def __init__(self):
        self.image_list = []
        self.dir = "none"

    def saveImg(self, dir, num, scores, crop_img_re, d, i):
        if(d[0][0] >= 0 and d[0][1] >= 0 and d[1][0] >= 0 and d[1][1] >= 0 and i == 0):
            img = cv2.cvtColor(crop_img_re, cv2.COLOR_RGB2GRAY)
            img = numpy.array(img)
            img = cv2.resize(img, (160, 90))
            face = [d[0][0], d[0][1], d[1][0], d[1][1]]
            self.image_list.append([img, face])
            if(self.dir == "none"):
                self.dir = dir

    def cropAndResize(self, frame, i, d):
        if(d[0][0] >= 0 and d[0][1] >= 0 and d[1][0] >= 0 and d[1][1] >= 0 and i == 0):
            self.crop_img = frame[d[0][1]:d[1][1],  d[0][0]: d[1][0]]
            self.crop_img_re = cv2.resize(self.crop_img, (48, 48))
            return self.crop_img_re

    def closeArchiver(self):
        loc = os.path.dirname(os.path.abspath(
            __file__)) + "/../" + self.dir + "/out.npy"
        numpy.save(loc, self.image_list)

    def getCurrentDir(self, line, experiment, loader):
        url = line
        if(int(loader) == 0):
            folder = re.findall("[^\=]*$", url)
            folder = folder[0]
            dir = "results/" + experiment + folder
        elif(int(loader) == 1):
            dir = "results/" + experiment + "imageStream"
        elif(int(loader) == 2):
            dir = "results/" + experiment + "videoStream"
        return dir, url
