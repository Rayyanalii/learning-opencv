import cv2 as cv
import numpy as np
from utils import rescaleFrame

image = cv.imread("Assets/Photos/red_deer.jpg")
resized_image = rescaleFrame(image,scale=0.25)
cv.imshow("Red Deer",resized_image)

gray = cv.cvtColor(resized_image,cv.COLOR_BGR2GRAY)
cv.imshow("Grayscale",gray)

# Laplacian
lap = cv.Laplacian(gray,cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("Laplacian",lap)

#Sobel 
sobelx = cv.Sobel(gray,cv.CV_64F,1,0)
sobely = cv.Sobel(gray,cv.CV_64F,0,1)
combined = cv.bitwise_or(sobelx,sobely)

cv.imshow("Sobel X",sobelx)
cv.imshow("Sobel Y",sobely)
cv.imshow("Combined Sobel",combined)

cv.waitKey(0)