import cv2 as cv
from utils import rescaleFrame
from utils import rotateFrame

image = cv.imread("Assets/Photos/red_deer.jpg")
resized_image = rescaleFrame(image,scale=0.25)

cv.imshow("Red Deer",resized_image)

rotate = rotateFrame(resized_image,-45)
cv.imshow("Rotate",rotate)

cv.waitKey(0)