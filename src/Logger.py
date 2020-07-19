class Logger:
    def logFaceCoordinates(self, i, d, scores, idx, visualize):
        print("\tL...Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(i, d[0][0], d[0][1], d[1][0], d[1][1]))
        print("\t\tL...score: {}, face_type:{}".format(round(scores[i],4), idx[i]))

    def logNumFaces(self, dets, percentage, vidid, filelength):
        print("Video " + str(vidid) + "/" + str(filelength) +  "| {:.2%} - "  "Number of faces detected this frame: {}".format(round((percentage), 4), len(dets)))
