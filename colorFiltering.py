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

	kernal = np.ones((15,15), np.float32)/255
	smooth = cv2.filter2D(res, -1, kernal)
	blur = cv2.GaussianBlur(res, (15,15), 0)
	median = cv2.medianBlur(res, 15)
	bilateral = cv2.bilateralFilter(res, 15,75,75)

	#cv2.imshow('freme', frame)
	#cv2.imshow('smooth', smooth)
	#cv2.imshow('mask', mask)
	#cv2.imshow('blur', blur)
	cv2.imshow('median', median)
	cv2.imshow('result', res)
	cv2.imshow('bilateral', bilateral)
 
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break
        
cv2.destroyAllWindows()
cap.release()
