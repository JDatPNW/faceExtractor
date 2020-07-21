import os
from .Initializer import Initializer

class clInitializer(Initializer):

    def getInput(self):
        self.visualize = input('Enable visualization? [1=Yes/0=No]: ')
        self.visualize = int(self.visualize)

        self.inputfile = input('Enter the name of the file containing the YouTube URLs: ')
        self.inputfile = "/input/" + self.inputfile
        self.inputfile = os.path.dirname(os.path.abspath(__file__)) + "/../" + self.inputfile

        self.experiment = input('Enter the name of the directory in which the video folders should be saved in: ')
        self.experiment =self.experiment + "/"

        self.threshold = input('Enter treshhold: ') #Default would be 0 - Cuts off after lower certanties

        self.sampling = input('Enter sampling: ') #1 works well

        self.tracker = input('Choose between dlib[1 - Recommended] and cv2[0] tracking: ') #1 works well


        return self.visualize, self.inputfile, self.experiment, self.threshold, self.sampling, self.tracker
