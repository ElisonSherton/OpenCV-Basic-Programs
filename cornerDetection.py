import cv2
import numpy as np

i = cv2.imread('toothpickShapes.png', 1)
grayI = cv2.cvtColor(i, cv2.COLOR_BGR2GRAY)

# Convert the integer values in the image to floating point values
gray = np.float32(grayI)

corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 5)
# cv2.goodFeaturesToTrack(image, max number of corners to find, image quality, minimum euclidean distance between two corners)
# Try varying the minimum distance between two corners and see it's influence on corner detection.
# Image must be 32 bit floting point with a single channel
# Each corner is qualified by a number. The quality determines which ones to keep w.r.t. the highest
# Quality corner. For eg. if the best corner quality is 1500, and you've mentioned 0.01 as the quality level,
# The corners with qualities less than 15 are not considered.

corners = np.int0(corners)

for c in corners:
    x, y = c.ravel()
    cv2.circle(i, (x,y), 3, 255, -1)

cv2.imshow('Corners', i)

cv2.waitKey()
cv2.destroyAllWindows()
