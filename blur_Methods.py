import cv2
import numpy as np

vid = cv2.VideoCapture(0)

while True:
    _, frame = vid.read()

    lower = np.array([150,0,0], np.uint8)
    upper = np.array([175,255,255], np.uint8)

    mask = cv2.inRange(frame, lower, upper)
    new_Frame = cv2.bitwise_and(frame, frame, mask = mask)

    cv2.imshow('Processed Frame', new_Frame)

    # The Gausssian Blur
    # cv2.GaussianBlur(sourceFrame, kernalSizeAsTuple, stdDev)
    # Kernal width and height must always be odd and positive
    gaus = cv2.GaussianBlur(new_Frame, (15,15), 0)
    cv2.imshow('Gaussian Blur', gaus)

    # The Median Blur
    # It is sharp with less noise
    # cv2.medianBlur(source, kernalSize, [destination])
    # kernalSize must be a positive odd number.
    median = cv2.medianBlur(new_Frame, 15)
    cv2.imshow('Median Blur', median)

    # The bilateral Blur
    bilateral = cv2.bilateralFilter(new_Frame, 15, 75, 75)
    cv2.imshow('Bilateral Blur', bilateral)

    # The mean blur
    kernal = np.ones((15,15), np.float32) / 255
    smoothed = cv2.filter2D(new_Frame, -1, kernal)

    k = cv2.waitKey(1)
    if k == 27:
        break

cv2.destroyAllWondows()
vid.release()
