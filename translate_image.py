import cv2 as cv
from utils import rescaleFrame
from utils import translate

image = cv.imread("Assets/Photos/red_deer.jpg")
resized_image = rescaleFrame(image,scale=0.25)

cv.imshow("Red Deer",resized_image)

translated = translate(resized_image,150,150)
cv.imshow("Translate",translated)

cv.waitKey(0)