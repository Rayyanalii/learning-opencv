import cv2 as cv

image = cv.imread("Assets/Photos/red_deer.jpg")

cv.imshow("Red Deer",image)

cv.waitKey(0)