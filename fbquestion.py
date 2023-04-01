# fb question
import numpy as np 
import cv2 

cap = cv2.VideoCapture('./CS551-Features.mov')
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.open 

if cap.isOpened()==False:
    print("error in opening video stream")
    exit()

fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('cut1.mp4', fourcc, 10, (800,400))

while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.flip(frame, 0)
        out.write(frame)
        cv2.imshow('frame', frame)
        print('playvideo')
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break 
    else:
        break 

cap.release()
out.release()
cv2.destroyAllWindows()