import cv2 as cv
import numpy as np
from utils import rescaleFrame

image = cv.imread("Assets/Photos/red_deer.jpg")
resized_image = rescaleFrame(image,scale=0.25)

blank = np.zeros(resized_image.shape[:2],dtype="uint8")

cv.imshow("Red Deer",resized_image)

b,g,r = cv.split(resized_image)

cv.imshow("Blue",b)
cv.imshow("Green",g)
cv.imshow("Red",r)

merged = cv.merge((b,g,r))
cv.imshow("Merge",merged)

blue = cv.merge((b,blank,blank))
cv.imshow("Blue Image",blue)

cv.waitKey(0)