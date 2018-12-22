import cv2
import numpy as np

i1 = cv2.imread('muellerGoal.jpg', 1)
i2 = cv2.imread('muellerGoalRotated.jpg', 1)
# Create an orb object and map the keypoints of the image
# Using these orb objects.
orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(i1, None)
kp2, des2 = orb.detectAndCompute(i2, None)

# Create a matcher object for comparison and use the method specified for comparison
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)
matches = bf.match(des1, des2)

# It is essential to sort before writing/displaying any image
# Because otherwise you'll get irrelevant matches.
matches = sorted(matches, key = lambda x:x.distance)

# Draw the matches onto another image for comparison.
i3 = cv2.drawMatches(i1, kp1, i2, kp2, matches[:20], None, flags = 2)
cv2.imshow("Matches", i3)

cv2.waitKey()
cv2.destroyAllWindows()
