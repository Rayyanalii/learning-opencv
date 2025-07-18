import cv2 as cv
import numpy as np

blank = np.zeros((500,500),dtype="uint8")

rectangle = cv.rectangle(blank.copy(),(50,50),(450,450),255,-1)
circle = cv.circle(blank.copy(),(250,250),250,255,-1)

cv.imshow("Rectangle",rectangle)
cv.imshow("Circle",circle)

bitwise_and = cv.bitwise_and(rectangle,circle)
cv.imshow("Bitwise AND",bitwise_and)

bitwise_or = cv.bitwise_or(rectangle,circle)
cv.imshow("Bitwise OR",bitwise_or)

bitwise_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow("Bitwise XOR",bitwise_xor)

bitwise_not = cv.bitwise_not(circle)
cv.imshow("Bitwise NOT",bitwise_not)

cv.waitKey(0)