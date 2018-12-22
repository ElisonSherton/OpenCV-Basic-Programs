import cv2
import numpy as np

video = cv2.VideoCapture('videoplayback.mp4')
# These cascade files are available on github.com
# https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
# https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_eye.xml

# Notice the capitalization of methods in cv2
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eyeCascade = cv2.CascadeClassifier('haarcascade_eye.xml')

while True:
    _, frame = video.read()
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Find the faces in a given frame
    faces = faceCascade.detectMultiScale(grayFrame)
    #In each frame, find the eye
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
        # Since rows are defined by y and columns are defined by x
        # Hence [rows,cols] = [y:y+h, x:x+w]
        roi_gray = grayFrame[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eyeCascade.detectMultiScale(roi_gray)
        for(ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (255,0,0), 2)

    cv2.imshow('Frame', frame)
    k = cv2.waitKey(10)
    if k == 27 or not _:
        break

video.release()
cv2.destroyAllWindows()
