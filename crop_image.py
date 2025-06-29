import cv2 as cv
from rescaleMethod import rescaleFrame

image = cv.imread("Assets/Photos/red_deer.jpg")
resized_image = rescaleFrame(image,scale=0.25)

cv.imshow("Red Deer",resized_image)
cropped = resized_image[0:500,50:1000]
cv.imshow("Cropped",cropped)

cv.waitKey(0)