import numpy as np
import cv2

img = cv2.imread('images.jpg', cv2.IMREAD_COLOR)

              #coordinates      #colour(bgr) #line-width
cv2.line(img, (0,0), (150,150), (255,0,0),  3)
cv2.rectangle(img, (15,25), (200,150), (0,255,0), 3)
cv2.circle(img, (100,63), 10, (0,0,255), -1)

pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2)) #-1 numpy figures out the dimensions you can only have one
cv2.polylines(img, [pts], True, (0,255,255), 3)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'openCV!', (0,130), font, 1, (255,0,255), 2, cv2.LINE_AA)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

