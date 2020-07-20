from .Visualizer import Visualizer
from .Loader import Loader
from .Initializer import Initializer
from .Archiver import Archiver
from .Tracker import Tracker
from .dlibTracker import dlibTracker
from .ocvTracker import ocvTracker
from .Logger import Logger
from .clInitializer import clInitializer
from .guiInitializer import guiInitializer
import os, cv2



class Main:
    def main(self):

        init = guiInitializer()
        visualize, inputfile, experiment, threshold, sampling = init.getInput()
        vis = Visualizer(visualize)
        log = Logger()
        load =  Loader()
        arch = Archiver()
        track = dlibTracker()
        track.initTracker()

        file = load.loadList(inputfile)
        vidid = 0
        filelength = load.getFileLength(file)
        file.seek(0)
        for line in file:
            vidid = vidid+1
            dir, url = arch.getCurrentDir(line, experiment)
            cap, best = load.loadStream(url)
            cap.open(best) #cap.open("./new_a/%05d.jpg") THIS WORKS FOR IMAGES!! need to only return the path in class
            num = 0;
            if not os.path.exists(dir):
                os.makedirs(dir)
                while(cap.isOpened()):
                    ret,frame = cap.read()
                    if (ret==True):
                        dets, scores, idx = track.detectFaces(frame, sampling, threshold)
                        log.logNumFaces(dets, (cap.get(cv2.CAP_PROP_POS_FRAMES)/ cap.get(cv2.CAP_PROP_FRAME_COUNT)), vidid, filelength)
                        for i, d in enumerate(dets):
                            log.logFaceCoordinates(i, d, scores, idx, visualize)
                            crop_img_re = arch.cropAndResize(frame, i, d)
                            arch.saveImg(dir, num, scores[i], crop_img_re, d)
                            vis.highlightFaces(frame, d)
                            num = num+1
                        stop = vis.displayVideo(frame)
                        if(stop):
                            break
                    else:
                        break
            vis.closeWindows()
            cap.release()

            print("#######################################")
            print("          Video {} done!               ".format(vidid))
            print("#######################################")
