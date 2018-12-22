import cv2
import numpy as np
video = cv2.VideoCapture('./sentdexVideos/Intro and loading Images  - OpenCV with Python for Image and Video Analysis 1.mp4')
# Create the background/foreground extractor object
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    _, frame = video.read()
    # Apply the extractor on the video frame
    mask = fgbg.apply(frame)
    # Use the extractor frame in order to obtain the feed
    # Which is actively moving/ changing that will be the forground
    # You can also use the not operator to indicate images in the background
    foregroundFrame = cv2.bitwise_and(frame, frame, mask = mask)
    backgroundFrame = cv2.bitwise_and(frame, frame, mask = cv2.bitwise_not(mask))
    cv2.imshow('Video', frame)
    # cv2.imshow('FGBG Mask', mask)
    # cv2.imshow('Foreground Frame', foregroundFrame)
    # cv2.imshow('Background Frame', backgroundFrame)
    k = cv2.waitKey()
    if k == 27 or not _:
        break

video.release()
cv2.destroyAllWindows()
