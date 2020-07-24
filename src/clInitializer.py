import os
from .Initializer import Initializer


class clInitializer(Initializer):

    def getInput(self):
        self.visualize = input('Enable visualization? [1=Yes/0=No]: ')
        self.visualize = int(self.visualize)

        self.inputfile = input(
            'Enter the name of the file(folder) containing the YouTube URLs/images/Video : ')
        self.inputfile = "/input/" + self.inputfile
        self.inputfile = os.path.dirname(
            os.path.abspath(__file__)) + "/.." + self.inputfile

        self.experiment = input(
            'Enter the name of the directory in which the video folders should be saved in: ')
        self.experiment = self.experiment + "/"

        # Default would be 0 - Cuts off after lower certanties
        self.threshold = input('Enter treshhold: ')

        self.sampling = input('Enter sampling: ')  # 1 works well

        self.logger = input(
            'Choose between Command Line Logging[1 - faster] and GUI Logging[0]: ')  # 1 works well

        self.loader = input(
            'Do you want to load a YouTube video[0], a folder of images[1], or a video file [2]?: ')  # 1 works well

        self.tracker = input(
            'Choose between dlib[1 - Recommended] and cv2[0] tracking: ')  # 1 works well

        self.visualizer = input(
            'Choose between the cv2[1 - fatser] and GUI[0] Visualizer: ')  # 1 works well

        self.archiver = input(
            'Do you want to safe the results as a .jpg[1] or as a .csv[0]: ')  # 1 works well

        if(int(self.visualize < 0)):
            self.visualize = 0
        elif(int(self.visualize) > 0 and int(self.visualize) < 1):
            self.visualize = 1
        elif(int(self.visualize) > 1):
            self.visualize = 1

        if(int(self.threshold) < 0):
            self.threshold = 0

        if(int(self.sampling) < 0):
            self.sampling = 0

        if(int(self.loader) < 0):
            self.loader = 0
        elif(int(self.loader) > 0 and int(self.loader) < 1):
            self.loader = 1
        elif(int(self.loader) > 1 and int(self.loader) < 2):
            self.loader = 1
        elif(int(self.loader) > 2):
            self.loader = 2

        if(int(self.logger) < 0):
            self.logger = 0
        elif(int(self.logger) > 0 and int(self.logger) < 1):
            self.logger = 1
        elif(int(self.logger) > 1):
            self.logger = 1

        if(int(self.tracker) < 0):
            self.tracker = 0
        elif(int(self.tracker) > 0 and int(self.tracker) < 1):
            self.tracker = 1
        elif(int(self.tracker) > 1):
            self.tracker = 1

        if(int(self.visualizer) < 0):
            self.visualizer = 0
        elif(int(self.visualizer) > 0 and int(self.visualizer) < 1):
            self.visualizer = 1
        elif(int(self.visualizer) > 1):
            self.visualizer = 1

        if(int(self.archiver) < 0):
            self.archiver = 0
        elif(int(self.archiver) > 0 and int(self.archiver) < 1):
            self.archiver = 1
        elif(int(self.archiver) > 1):
            self.archiver = 1

        return (self.visualize,
                self.inputfile, self.experiment, self.threshold, self.sampling, self.tracker,
                self.logger, self.visualizer, self.loader, self.archiver)
