from .ocvVisualizer import ocvVisualizer
from .guiVisualizer import guiVisualizer
from .imgLoader import imgLoader
from .vidLoader import vidLoader
from .ytLoader import ytLoader
from .jpgArchiver import jpgArchiver
from .csvArchiver import csvArchiver
from .dlibTracker import dlibTracker
from .ocvTracker import ocvTracker
from .guiLogger import guiLogger
from .cliLogger import cliLogger
from .clInitializer import clInitializer
from .guiInitializer import guiInitializer
import os
import cv2


class Main:
    def __init__(self, mode):
        self.mode = mode

    def main(self):

        if(self.mode == "gui"):
            init = guiInitializer()
        else:
            init = clInitializer()

        visualize, inputfile, experiment, threshold, sampling, tracker, logger, visualizer, loader, archiver = init.getInput()

        if(int(logger) == 1):
            log = cliLogger()
        else:
            log = guiLogger()

        if(int(visualizer) == 1):
            vis = ocvVisualizer(visualize, log)
        else:
            vis = guiVisualizer(visualize, log)

        if(int(loader) == 1):
            load = imgLoader()
        elif(int(loader) == 2):
            load = vidLoader()
        else:
            load = ytLoader()
        if(int(archiver) == 0):
            arch = csvArchiver()
        else:
            arch = jpgArchiver()

        if(int(tracker) == 1):
            track = dlibTracker()
        else:
            track = ocvTracker()

        track.initTracker()

        file = load.loadList(inputfile)
        vidid = 0
        filelength = load.getFileLength(file)
        if(loader == 0):
            file.seek(0)
        for line in file:
            vidid = vidid + 1
            dir, url = arch.getCurrentDir(line, experiment, loader)
            cap, best = load.loadStream(url)
            cap.open(best)
            num = 0
            vis.setupWindow()
            if not os.path.exists(dir):
                os.makedirs(dir)
                while(cap.isOpened()):
                    ret, frame = cap.read()
                    if (ret is True):
                        dets, scores, idx = track.detectFaces(
                            frame, sampling, threshold)
                        log.logNumFaces(dets, (cap.get(
                            cv2.CAP_PROP_POS_FRAMES) / cap.get(cv2.CAP_PROP_FRAME_COUNT)), vidid, filelength)
                        for i, d in enumerate(dets):
                            log.logFaceCoordinates(
                                i, d, scores, idx, visualize)
                            crop_img_re = arch.cropAndResize(frame, i, d)
                            arch.saveImg(dir, num, scores[i], crop_img_re, d)
                            vis.highlightFaces(frame, d)
                            num = num + 1
                        stop = vis.displayVideo(frame)
                        if(stop):
                            break
                    else:
                        break
            cap.release()
            vis.closeWindows()
            arch.closeArchiver()
            print("#######################################")
            print("          Video {} done!               ".format(vidid))
            print("#######################################")

        log.end()
