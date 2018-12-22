import cv2
import numpy as np

frame = cv2.imread('L.jpg', cv2.IMREAD_GRAYSCALE)
count = 1

while(True):
    laplacian = cv2.Laplacian(frame, cv2.CV_64F)


    sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize = count)
    sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize = count)
    sobelxy = cv2.Sobel(frame, cv2.CV_64F, 1, 1, ksize = count)

    # Sobel operator is meant to work only on grayscale images.
    # The kernel size in the operator must always be odd.
    # Watch this computerphile video to find our why...
    # https://www.youtube.com/watch?v=uihBwtPIBxM
    # CV_64F = 64F - Double, 32F - float, 8U - unsigned char

    cannyEdges = cv2.Canny(frame, 100, 200)
    LImage = cv2.bitwise_not(cannyEdges)

    cv2.imshow('Laplacian',laplacian)
    cv2.imshow('SobelX', sobelx)
    cv2.imshow('SobelY', sobely)
    cv2.imshow('SobelXY', sobelxy)
    cv2.imshow('Canny Edges', LImage)

    k = cv2.waitKey(100)
    if k == 27:
        break

    if count > 21:
        count = 3
    else:
        pass
        #count = count + 2

cv2.destroyAllWindows()
