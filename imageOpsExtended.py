import cv2
import numpy as np

image = cv2.imread('L.jpg', cv2.IMREAD_COLOR)
#https://docs.opencv.org/3.4/d4/da8/group__imgcodecs.html#ga288b8b3da0892bd651fce07b3bbd3a56

#You can read and/or write any pixel in a given image as follows
image[30,30] = [255,0,0]
#image[x_loc, y_loc] = [B_as_int, G_as_int, R_as_int]
print(image[30,30]) # ---> To read the color value at any given location in an image

#ROI ---> Region of an image
#Instead of working with individual pixels, you can work with a bunch of
#them simultaneously as below

L_hand = image[170:230, 130:200]    # MATLAB-esque indexing works well here!
image[0:60, 0:70] = L_hand          # i.e. To say a to b, you can use a:b
#cv2.imshow('L Hand', image)

width = image.shape[0]
height = image.shape[1]

Left = image[0:width, 0:int(height/2)]
Right = image[0:width, int(height/2):height]
print(width,height)
i = np.zeros((width,height,3),np.uint8)
i[0:width,0:int(height/2)] = Right
i[0:width, int(height/2):height] = Left
cv2.imshow('L', i)

#*****NOTE******
#The indexing is done y first and then x, not the other way round.
#IN p5.js and Processing, it is done with x first and then y, so don't get confused!

#This code copies all the pixel colors from the region specified to be L_hand
#And it writes it onto the top left corner of the Image
#The area of ROI to be modified and ROI from which we read the pixels must be the same!


Face = image[20:150, 20:160]
image[0:130,0:140] = Face
cv2.imshow('L Face', image)

cv2.waitKey(0)
cv2.destroyAllWindows()
