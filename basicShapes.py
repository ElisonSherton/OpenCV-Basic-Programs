import cv2
import numpy as np
ScreenWidth = 1280
ScreenHeight = 480

image = cv2.imread('L.jpg', cv2.IMREAD_COLOR)

# Drawing a line on an Image

cv2.line(image, (150,0), (150,150) , (255,255,255) , 4)
#cv2.line(img, start_point_as_Tuple, end_point_as_Tuple, BGR_Color_as_tuple, lineWidth_as_Integer)

cv2.rectangle(image, (25,25), (50,50), (255,0,0), 5)
#cv2.line(img, top_left_coord_as_Tuple, bottom_right_coord_as_Tuple, BGR_Color_as_tuple, lineWidth_as_Integer)

cv2.circle(image, (150,150) , 25, (0,0,255) , 1)
#cv2.circle(img, center_as_Tuple, radius_as_Integer, BGR_Color_as_tuple, lineWidth_as_Integer)
#For negative linewidths, the circle will be filled, else, it will only be outlined.

points = np.array([[20,20], [30,30], [10,4], [0,50], [0,0]], np.int32)
cv2.polylines(image, [points], True, (0,255,0), 1)
#cv2.polylines(image, array of co-ordinates, BGR_Color_as_tuple, line_width)

font = cv2.FONT_HERSHEY_PLAIN
cv2.putText(image, 'L', (50,50), font, 1, (200,0,200), 2)
#cv2.putText(img, txt_As_String, start_As_Tuple, font_As_cv2.FONT_XXX, text_Size, BGR_Color_as_tuple,text_Thickness_As_int, cv2.LINE_AA)
#Lasr argument for line anti-aliasing sake is optional

cv2.imshow('L Thinking', image)
#cv2.imshow to draw an Image

cv2.moveWindow("L Thinking",int(ScreenWidth/2),int(ScreenHeight/2))
#cv2.moveWindow(window_Name_As_String, x_point_As_int, y_point_As_int)

cv2.waitKey(0)
#cv2.waitKey(int) to freeze the screen until the user hits a key

cv2.destroyAllWindows()
#Eventually, close all windows before you quit the system
