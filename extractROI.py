import cv2
import numpy as np

image = cv2.imread('Good.png', 1)
roi = image[280:400, 115:290]
rows, cols, channels = image.shape
i = np.zeros((rows,cols,channels),np.uint8)
j = np.zeros((rows,cols,channels),np.uint8)

xtl = cols - (290-115)
ytl = rows - (400-280)

i[ytl:rows, xtl:cols] = roi
j[0:120, 0:175] = roi
print(rows, cols, channels)

print(290-115, cols-xtl)
print(400-280, rows-ytl)

cv2.imshow("Good", image)
cv2.imshow("Extracted Image", i)
cv2.imshow("Extracted Image Top Left", j)
cv2.waitKey()
cv2.destroyAllWindows()
