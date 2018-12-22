import cv2
import numpy as np

video = cv2.VideoCapture('videoplayback.mp4')

while True:
    ret_val, frame = video.read()

    lower = np.array([200,200,200], np.uint8)
    upper = np.array([255,255,255], np.uint8)

    mask = cv2.inRange(frame, lower, upper)
    disp_Frame = cv2.bitwise_and(frame, frame, mask = mask)

    kernel = np.ones((5,5), np.uint8)
    erosion = cv2.erode(mask, kernel, iterations = 1)
    dilation = cv2.dilate(mask, kernel, iterations = 1)

    cv2.imshow('Display Frame', disp_Frame)
    cv2.imshow('Erosion', erosion)
    cv2.imshow('Dilation', dilation)

    k = cv2.waitKey(33)
    if k == 27:
        break

cv2.destroyAllWindows()
video.release()
