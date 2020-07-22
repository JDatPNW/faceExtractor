from src.main import Main
import sys
import getopt


def getArgs(argv):
    mode = "cl"
    try:
        opts, args = getopt.getopt(argv, "-gui,-h,-cl")
    except getopt.GetoptError:
        print ('Incorrect flags, try running faceTracker.py -h')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('faceTracker.py -gui | run faceTracker with GUI')
            print ('faceTracker.py -cl | run faceTracker in the Command Line')
            sys.exit()
        elif opt in ("-gui"):
            mode = "gui"
        elif opt in ("-cl"):
            mode = "cl"
    return mode


if __name__ == "__main__":
    print("#######################################")
    print("#######################################")
    print("########      FaceTracker      ########")
    print("#######################################")
    print("#######################################\n")

    thisFaceTracker = Main(getArgs(sys.argv[1:]))
    thisFaceTracker.main()

    print("Done! All videos are finished.")
