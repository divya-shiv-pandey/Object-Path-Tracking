from collections import deque
from imutils.video import VideoStream
import numpy as np
import argparse
import cv2
import imutils
import time

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
    help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=32,
    help="max buffer size")
args = vars(ap.parse_args())

cap = cv2.VideoCapture(0)

pts = deque(maxlen=args["buffer"])


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface.xml')
while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.25,5)
    for(x,y,w,h) in faces:
        point = (int((x + x+w)/2),int((y + y +h)/2))
        f = open("face.txt","a+")
        f.write(str(int((x + x+w)/2))+ " ")
        f.write(str(int((y + y +h)/2))+ "\n")
        #f.write(str(list(point))+"\n")
        f.close()
        cv2.circle(img, point, radius=2, color=(0, 0, 255), thickness=-1)
        pts.appendleft(point)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
   
    for i in np.arange(1, len(pts)):
        thickness = int(np.sqrt(args["buffer"] / float(i + 1)) * 2.5)
        cv2.line(img, pts[i - 1],pts[i], (0, 0, 255), thickness)
        
    cv2.imshow('img',img)
    k = cv2.waitKey(2) & 0xff
    if k == 32:
        break
    

cap.release()
cv2.destroyAllWindows()


