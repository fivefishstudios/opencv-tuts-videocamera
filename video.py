# video.py
# 6.21.22
# all about video processing
# like play video, save video, capture video

import cv2 as cv
import numpy as np 

# open the file 
vid = cv.VideoCapture('./july7 testing-mp4v-15fps-1280-720.mp4')

# while file is open, do the following loop
while vid.isOpened():
    # read frame of video file
    ret, frame = vid.read()

    # is frame valid? check the return value
    if not ret:
        print("End of file... exiting")
        break 

    # we got a successful frame read
    # we can do further processing here before displaying the frame
    frame = cv.cvtColor(frame,cv.COLOR_BGR2HSV)

    # display in window (note: there will be no sound)
    cv.imshow("My Video", frame)
    # wait for keypress 'q' to exit
    if cv.waitKey(1) == ord('q'):
        break 

# close video file 
vid.release() 

# close any window created
cv.destroyAllWindows()