import cv2 as cv
from utils import rescaleFrame

image = cv.imread("Assets/Photos/red_deer.jpg")
resized_image = rescaleFrame(image,scale=0.25)

cv.imshow("Red Deer",resized_image)

flip = cv.flip(resized_image,-1)
cv.imshow("Flipped",flip)

cv.waitKey(0)