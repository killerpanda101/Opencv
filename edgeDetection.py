import numpy as np 
import cv2

cap = cv2.VideoCapture(0)

while True:
	_, frame = cap.read()

	#both the x and y gradient
	laplacian = cv2.Laplacian(frame, cv2.CV_64F)
	#x seperated
	sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)
	#y seperated
	sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)

	cv2.imshow('laplacian', laplacian)
	cv2.imshow('sobelx', sobelx)
	cv2.imshow('sobely', sobely)
	
 
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break
        
cv2.destroyAllWindows()
cap.release()