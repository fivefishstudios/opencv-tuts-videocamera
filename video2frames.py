# savevideo.py
# 6.21.22
# all about video processing
# like play video, save video, capture video


import cv2 as cv
import numpy as np 

sequence = 0 

# open the file (or the video usb camera)
usbcamera = 0
vid = cv.VideoCapture(usbcamera)

# read and display one frame
ret, frame = vid.read()

# if we're resaving this video, create a VideoWriter 
# videoformat = 0  # save as individual frames
videoformat = cv.VideoWriter_fourcc(*'XVID')  # .mp4
# other formats for Mac OSX, note *'MJPG' is the same as ('M','J','P','G')
# videoformat = cv.VideoWriter_fourcc(*'MJPG')   # .mp4 (does not play in quicktime, play in VLC)
# videoformat = cv.VideoWriter_fourcc(*'DIVX')   # .avi 
# videoformat = cv.VideoWriter_fourcc(*'X264')   # .mkv 
# fps = int(vid.get(cv.CAP_PROP_FPS))  # fps 
fps = 15  # 15fps seems to be the normal speed 
width  = int(vid.get(cv.CAP_PROP_FRAME_WIDTH))  # float `width`
height = int(vid.get(cv.CAP_PROP_FRAME_HEIGHT))  # float `height`
framesize = (width, height)
filepath = "./videocapture/"
filenameOut = filepath + 'img_%03d.jpg'%(sequence+1)
videoOutput =  cv.VideoWriter(filenameOut, videoformat, fps, framesize)

# while file (or camera) is open, do the following loop
while vid.isOpened():
    sequence = sequence + 1 
    filenameOut = filepath + 'img_%03d.jpg'%(sequence)
    # read frame of video file
    ret, frame = vid.read()

    # is frame valid? check the return value
    if not ret:
        print("End of file... exiting")
        break 

    # we got a successful frame read
    # we can do further processing here before displaying the frame
    # frame = cv.cvtColor(frame,cv.COLOR_BGR2HSV) # this works as mp4 output format
    # frame = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

    # write the frame
    # videoOutput.write(frame)
    result = cv.imwrite(filenameOut, frame)

    # display in window (note: there will be no sound)
    cv.imshow("My Video", frame)
    # wait for keypress 'q' to exit
    if cv.waitKey(1) == ord('q'):
        break 

# close video output file
videoOutput.release()
# close video file 
vid.release() 

# close any window created
cv.destroyAllWindows()