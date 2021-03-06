import cv2
import numpy as np

i1 = cv2.imread('youTubelogo.jpg', cv2.IMREAD_COLOR)
i2 = cv2.imread('shiffman.png', cv2.IMREAD_COLOR)
#ROI = Region of Interest
rows, cols, chn = i1.shape
ROI = i2[0:rows, 0:cols]
#Convert the image to a grayscale Image
i1Gray = cv2.cvtColor(i1, cv2.COLOR_BGR2GRAY)

# Threshold the grayScale image to black out the irrelevant
# And whiteout the relevent
ret, i1Thold = cv2.threshold(i1Gray, 10, 255, cv2.THRESH_BINARY)

# Also create an inverse of the thresholded image
i1Inverse = cv2.bitwise_not(i1Thold)

# From the background of cut piece of destination Image
# Use the inverse mask to black out the i1 part
i2_bg = cv2.bitwise_and(ROI, ROI, mask = i1Inverse)

# Use the thresholded image to black out the
# background from original image.
i1_fg = cv2.bitwise_and(i1, i1, mask = i1Thold)

# Add the two images of foreground and background together
final = cv2.add(i1_fg, i2_bg)

# Superimpose processed part on the region of interest of the image
i2[0:rows, 0:cols] = final

cv2.imshow('Final', i2)
cv2.imshow('Added', final)
cv2.waitKey(0)
cv2.destroyAllWindows()
