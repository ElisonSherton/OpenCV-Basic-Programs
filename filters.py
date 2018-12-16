#Official Documentation - https://docs.opencv.org/3.4/d7/d4d/tutorial_py_thresholding.html
import cv2
import numpy as np

i = cv2.imread('testImage.jpg', cv2.IMREAD_COLOR)
# Binary Filter
iGray = cv2.cvtColor(i, cv2.COLOR_BGR2GRAY)
ret, i_Bin = cv2.threshold(iGray, 150, 255, cv2.THRESH_BINARY)
cv2.imshow('Binary Threshold', i_Bin)

# Adaptive Gaussian Filter
# cv2.adaptiveThreshold(src_image, maxVal, adaptive method, threshold_type, window/block size, constant)
# adaptive method - ADAPTIVE_THRESH_GAUSSIAN_C, ADAPTIVE_THRESH_MEAN_C
# window/block size - How many neighboriing elements influence this portion of the image
# constant - Just a constant value that is subtracted from the mean value
gaus = cv2.adaptiveThreshold(iGray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 47, 1)
cv2.imshow('Gaussian Threshold', gaus)

# Adaptive Otsu's filter
# Used for bimodal image, i.e. an image with exactly two peaks
retval , i_otsu = cv2.threshold(iGray, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow('Otsu Threshold', i_otsu)

cv2.waitKey(0)
cv2.destroyAllWindows()
