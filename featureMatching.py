#better version of template matching

import numpy as np 
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('stickers.jpg', 0)
tongue = cv2.imread('capture.jpg',0)

orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(img, None)
kp2, des2 = orb.detectAndCompute(tongue, None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)

matches = bf.match(des1, des2)
matches = sorted(matches, key = lambda x:x.distance)

img3 = cv2.drawMatches(img, kp1, tongue, kp2, matches[8:9], None, flags=2)
plt.imshow(img3)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

#matplot lib is rgb and open cv is bgr

