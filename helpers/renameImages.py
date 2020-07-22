import os
from PIL import Image
import glob
import shutil


def getFileName(currentImage):
    digits = len(str(currentImage))
    prefix = ""
    for i in range(5 - digits):
        prefix = prefix + "0"
    name = prefix + str(currentImage)
    return name


def PNGtoJPG(dir):
    for file in list(glob.glob(dir + '*.png')):
        png = Image.open(file)
        png = png.convert("RGB")
        png.save(file + ".jpg")
        os.remove(file)


def main():
    foldername = input('Enter the name of the folder containing the images: ')
    dir = os.path.dirname(os.path.abspath(__file__))
    newdir = dir + "/../input/new_" + foldername + "/"
    dir = dir + "/../input/" + foldername + "/"
    PNGtoJPG(dir)
    if not os.path.exists(newdir):
        os.makedirs(newdir)
    for count, filename in enumerate(os.listdir(dir)):
        newName = getFileName(count + 1)
        dst = newName + ".jpg"
        src = dir + filename
        dst = newdir + dst
        shutil.copyfile(src, dst)


main()
