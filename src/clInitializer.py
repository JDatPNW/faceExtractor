import os
from .Initializer import Initializer


class clInitializer(Initializer):

    def getInput(self):
        self.visualize = input('Enable visualization? [1=Yes/0=No]: ')
        self.visualize = int(self.visualize)

        self.inputfile = input(
            'Enter the name of the file containing the YouTube URLs: ')
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
            'Do you want to load a YouTube video[0] or a folder of images[1]?: ')  # 1 works well

        self.tracker = input(
            'Choose between dlib[1 - Recommended] and cv2[0] tracking: ')  # 1 works well

        self.visualizer = input(
            'Choose between the cv2[1 - fatser] and GUI[0] Visualizer: ')  # 1 works well

        return (self.visualize,
                self.inputfile, self.experiment, self.threshold, self.sampling, self.tracker,
                self.logger, self.visualizer, self.loader)
