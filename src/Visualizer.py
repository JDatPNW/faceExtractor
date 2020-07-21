import numpy, cv2

class Visualizer:

    def __init__(self, vis):
        self.visualize = vis

    def setupWindow(self):
        if(self.visualize==1):
            cv2.namedWindow('FaceExtractor Video Feed', cv2.WINDOW_NORMAL)

    def displayVideo(self, frame):
        if(self.visualize==1):
            cv2.imshow('FaceExtractor Video Feed',numpy.array(frame, dtype = numpy.uint8))
            if cv2.waitKey(5) & 0xFF == ord('q'):
                return 1
            else:
                return 0

    def highlightFaces(self, frame, d):
        if(self.visualize==1):
            cv2.rectangle(frame, (d[0][0], d[0][1]), (d[1][0], d[1][1]), (255, 0, 0), 2)

    def closeWindows(self):
        if (self.visualize==1):
            cv2.destroyAllWindows()
