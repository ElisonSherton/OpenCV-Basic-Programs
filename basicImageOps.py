import cv2

#To read an image, use the imread function
image = cv2.imread('L.jpg',0)
# imread also accepts a second argument for different ways in which
# want to load a file in computer's memory
# cv2.IMREAD_GRAYSCALE  = 0
# cv2.IMREAD_COLOR      = 1
# cv2.IMREAD_UNCHANGED  = -1


#To display an image to the screen, use the imshow function
cv2.imshow('Image',image)
# cv2.waitKey(int)
# If the argument is > 0, it waits for that many milliseconds for
# a key input before it stops displaying on the screen.
# If argument <=0, it waits infinitely for a key input
cv2.waitKey()
#Close all the active windows which you have drawn on the screen
cv2.destroyAllWindows()

#To save an image, use the imwrite function
cv2.imwrite('L1.jpg',image)
