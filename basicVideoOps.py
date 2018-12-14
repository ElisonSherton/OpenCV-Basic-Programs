import cv2
import numpy as np

video = cv2.VideoCapture('videoplayback.mp4')
while (True):
    ret, frame = video.read()
    print(ret)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
