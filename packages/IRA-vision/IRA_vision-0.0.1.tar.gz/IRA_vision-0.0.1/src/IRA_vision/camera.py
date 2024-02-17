import cv2
import numpy as np
import time

def image(index=0,size=[640,480],mode='rgb',T=1):
    cap = cv2.VideoCapture(index)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, size[0])
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, size[1])
    t1=time.time()
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        key = cv2.waitKey(1) & 0xFF
        t2=time.time()
        if t2-t1 >= T:
            if mode == 'gray':
                grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                cv2.imwrite('captured.jpg', grayFrame)
                break
            elif mode=='rgb':
                cv2.imwrite('captured.jpg', frame)
                break    
    cap.release()
def video(index=0,size=[640,480]):
    cap = cv2.VideoCapture(index)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, size[0])
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, size[1])
    while True:
        ret, frame = cap.read()
        cv2.imshow('video',frame)
        if not ret:
            break
        key = cv2.waitKey(1) & 0xFF
        if key==27:
            break
    cap.release()
    cv2.destroyAllWindows()