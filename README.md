![](https://github.com/JDatPNW/faceExtractor/blob/master/src/imgs/icon.ico)
# faceTrack
A framework which allows to collect data (faces) for machine- and  deep-learning algorithms, from:
* YouTube videos
* Images (all in 1 folder)
* Video files (saved locally)

This was meant to help with class projects that require big data-sets, which can sometimes be hard and tedious to come by.

If you want to run it on a YouTube video, create a .txt file in the input folder, that contains all your YouTube URLs, one each line (no empty lines).
Your video files and pictures should also be saved within that folder. Make sure that the folder the images are in, does not contain any other files.
When using the Command Line Initializer, all paths are relative to the corresponding folder (input or results)

To use the GUI Initializer, run "python faceTracking.py -gui", running it without the Flag will trigger the Command Line Initializer.
Just follow the instructions given to you by the program, to successfully extract the data.
