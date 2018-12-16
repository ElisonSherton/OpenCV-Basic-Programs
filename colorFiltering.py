import cv2
import numpy as np

vid = cv2.VideoCapture(0)

while True:
    _, frame = vid.read()
    rows, cols, channels = frame.shape
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Lower and upper bounds on the hue are decided below
    # This filters out only blueberry pulp kind of color
    # which also looks like black grapes' pulp

    lower = np.array([125,0,0])
    upper = np.array([150,255,255])
    # The inRange function checks if the pixels in a Frame
    # Lie within a given range of colors and optionally
    # colors a dest frame where all are ones and discards all 0 values.
    # inRange(source, lower, upper, destination)
    mask = cv2.inRange(hsv, lower, upper)
    disp_Frame = cv2.bitwise_and(frame, frame, mask = mask)
    cv2.imshow('Display Frame', disp_Frame)
    cv2.imshow('Mask', mask)
    cv2.imshow('Original Frame', frame)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    print(rows,cols,channels)

cv2.destroyAllWindows()
vid.release()
