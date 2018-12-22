import cv2
import numpy as np

i =cv2.imread('L.jpg')
mask = np.zeros(i.shape[:2], np.uint8)
print(i.shape[:2])

bgModel = np.zeros((1,65), np.float64)
fgModel = np.zeros((1,65),np.float64)

# The region which you are interested in is defined here.
rect = (20,20,150,170)

cv2.grabCut(i, mask, rect, bgModel, fgModel, 5, cv2.GC_INIT_WITH_RECT)

# First the input image, then the mask, then the rectangle for our main object,
# the background model, foreground model, the amount of iterations to run,
# and what mode you are using i.e. initialize with rect or mask

# Make a note of the syntax appropriately
# The mask comparison in np.where can be deceptive.
# The combination of "or" with comparison operator needs to be written
# in a meticulous way else, it will raise numerous errors.
mask2 = np.where((mask == 0) | (mask == 2), 0, 1).astype('uint8')
i1 = i*mask2[:,:,np.newaxis]

cv2.imshow("Image", i1)
cv2.imshow("Original", i)
cv2.waitKey()
cv2.destroyAllWindows()
