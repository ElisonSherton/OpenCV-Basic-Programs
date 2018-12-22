import cv2
import numpy as np

template = cv2.imread('template.png', cv2.IMREAD_GRAYSCALE)
toSearch = cv2.imread('toSearchFrom.png', cv2.IMREAD_COLOR)
toSearchGray = cv2.cvtColor(toSearch, cv2.COLOR_BGR2GRAY)

w, h = template.shape[::-1]
result = cv2.matchTemplate(toSearchGray, template, cv2.TM_CCOEFF_NORMED)
# Other methods of comparison to do template searching
# cv2.TM_CCOEFF, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF,
# cv2.TM_SQDIFF_NORMED, cv2.TM_CCORR

ths = 0.99
print(result)
loc = np.where(result >= ths)

for i in zip(*loc[::-1]):
    cv2.rectangle(toSearch, i, (i[0] + w, i[1] + h), (0,255,255), 2 )

cv2.imshow('Detected Frame', toSearch)

cv2.waitKey()
cv2.destroyAllWindows()
