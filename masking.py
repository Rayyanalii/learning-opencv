import cv2 as cv
import numpy as np
from utils import rescaleFrame

image = cv.imread("Assets/Photos/red_deer.jpg")
resized_image = rescaleFrame(image,scale=0.25)

cv.imshow("Red Deer",resized_image)

blank = np.zeros(resized_image.shape[:2],dtype="uint8")

mask = cv.circle(blank, (resized_image.shape[1]//2,resized_image.shape[0]//2),100,255,-1)
cv.imshow("Mask",mask)

masked = cv.bitwise_and(resized_image,resized_image,mask=mask)
cv.imshow("Masked",masked)

cv.waitKey(0)