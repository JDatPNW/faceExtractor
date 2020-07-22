import cv2
import re
import PIL
import csv
import os
from .Archiver import Archiver


class csvArchiver(Archiver):

    def __init__(self):
        self.image_list = []
        self.dir = "none"

    def saveImg(self, dir, num, scores, crop_img_re, d):
        if(d[0][0] >= 0 and d[0][1] >= 0 and d[1][0] >= 0 and d[1][1] >= 0):
            img = cv2.cvtColor(crop_img_re, cv2.COLOR_BGR2RGB)
            img = PIL.Image.fromarray(img)
            img = img.convert('RGB')
            pixels = list(img.getdata())
            pixels = [item for t in pixels for item in t]
            self.image_list.append(pixels)
            if(self.dir == "none"):
                self.dir = dir

    def cropAndResize(self, frame, i, d):
        if(d[0][0] >= 0 and d[0][1] >= 0 and d[1][0] >= 0 and d[1][1] >= 0):
            self.crop_img = frame[d[0][1]:d[1][1],  d[0][0]: d[1][0]]
            self.crop_img_re = cv2.resize(self.crop_img, (48, 48))
            return self.crop_img_re

    def closeArchiver(self):
        loc = os.path.dirname(os.path.abspath(
            __file__)) + "/../" + self.dir + "/out.csv"
        with open(loc, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(self.image_list)

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
