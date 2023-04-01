# video_play_backwards.py 
# Play video file backwards
# 6.23.22 

import cv2 

# setup camera or video file
videofilename = './SA-IG.mp4'
capture = cv2.VideoCapture(videofilename)

# get total frames 
total_frames = capture.get(cv2.CAP_PROP_FRAME_COUNT)

# start at last frame 
frame_ndx = total_frames - 10

while frame_ndx > 0:
    # go to frame ndx
    capture.set(cv2.CAP_PROP_POS_FRAMES, frame_ndx)
    # read frame 
    ret, frame = capture.read()

    # display
    cv2.imshow('Playback', frame)
    cv2.waitKey(1)  #waitKey() so we can see the window/video 

    frame_ndx = frame_ndx - 5   # use higher decrement to speed up video and skip frames

# wait for keypress
cv2.waitKey(0)

# release everything 
capture.release()
cv2.destroyAllWindows()