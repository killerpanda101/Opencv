import numpy as np 
import cv2 
 
img = cv2.imread('images.jpg', cv2.IMREAD_COLOR)


px = img[55,55] #color value for that pixel
px = [255,255,255] #now a white pixel

#region of an image(roi) sub-image of an image 
roi = img[0:45, 0:45] = [255,255,255]

#copy and paste using roi
roi_logo = img[120:200, 35:120]
img[0:80,0:85] = roi_logo



cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
