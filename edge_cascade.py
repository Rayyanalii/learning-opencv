import cv2 as cv
from rescaleMethod import rescaleFrame

image = cv.imread("Assets/Photos/red_deer.jpg")
resized_image = rescaleFrame(image,scale=0.25)

cv.imshow("Red Deer",resized_image)

blur = cv.GaussianBlur(resized_image,(11,11),cv.BORDER_DEFAULT)
cv.imshow("Blur",blur)

# Pass the blurred image to reduce the number of edges found

canny = cv.Canny(resized_image,125,175)
cv.imshow("Canny Edges",canny)

cv.waitKey(0)