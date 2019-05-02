#works by finding changes form the previous
# frame and makes that as the forground

import numpy as np 
import cv2

cap = cv2.VideoCapture('song.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
 	ret,frame = cap.read()
 	fgmask = fgbg.apply(frame)

 	cv2.imshow('original', frame)
 	cv2.imshow('forground', fgmask)

 	k = cv2.waitKey(30) & 0xff
 	if k == 27:
 		break

cap.release()
cv2.destroyAllWindows()
