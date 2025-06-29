import cv2 as cv
import numpy as np

from utils import rescaleFrame

image = cv.imread("Assets/Photos/red_deer.jpg")
resized_image = rescaleFrame(image,scale=0.25)

cv.imshow("Red Deer",resized_image)
blank = np.zeros(resized_image.shape)
cv.imshow("Blank",blank)

gray = cv.cvtColor(resized_image,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

# blur = cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
# cv.imshow("Blur",blur)

# canny = cv.Canny(blur,125,175)
# cv.imshow("Canny Edges",canny)

# Using Thresh
ret, thresh = cv.threshold(gray,125,255,type=cv.THRESH_BINARY)
cv.imshow("Thresh",thresh)

contours, hierarchies = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(len(contours))

cv.drawContours(blank,contours,-1,(255,0,0),1)
cv.imshow("Blank",blank)

cv.waitKey(0)