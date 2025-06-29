import cv2 as cv
from utils import rescaleFrame

image = cv.imread("Assets/Photos/red_deer.jpg")
resized_image = rescaleFrame(image,scale=0.25)

cv.imshow("Red Deer",resized_image)

gray = cv.cvtColor(resized_image,cv.COLOR_BGR2GRAY)
cv.imshow("Grayscale",gray)

cv.waitKey(0)