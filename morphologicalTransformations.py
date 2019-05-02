import numpy as np 
import cv2

cap = cv2.VideoCapture(0)

while True:
	_, frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	lower_red = np.array([0,50,100])
	upper_red = np.array([30,140,255])

	mask = cv2.inRange(hsv, lower_red, upper_red)
			   #something on the frame 	#that specifies elements of the output array to be changed.
	res = cv2.bitwise_and(frame, frame, mask = mask)

	kernal = np.ones((5,5), np.uint8)
	 #takes a pixel checks with the nearby pixel if colour does not match then it erodes away
	erosion = cv2.erode(mask, kernal, iterations=1)
	 #dialation pushes out the colour trying to fill in the pixels
	dilation = cv2.dilate(mask, kernal, iterations=1)

	#opening is used to remove false positives(background noise)
	opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)
	#closing is to add in the place of false negetives
	closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)

	cv2.imshow('freme', frame)
	cv2.imshow('result', res)
	#cv2.imshow('erosion', erosion)
	#cv2.imshow('dilation', dilation)
	
	#there is also top hat and black hat(difference between the opening or closing of the image)
 
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break
        
cv2.destroyAllWindows()
cap.release()