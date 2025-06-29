import cv2 as cv
from utils import rescaleFrame

image = cv.imread("Assets/Photos/red_deer.jpg")
resized_image = rescaleFrame(image,scale=0.25)

cv.imshow("Red Deer",resized_image)

# BGR to Gray
gray = cv.cvtColor(resized_image,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

# BGR to HSV
hsv = cv.cvtColor(resized_image,cv.COLOR_BGR2HSV)
cv.imshow("HSV",hsv)

# BGR to LAB
lab = cv.cvtColor(resized_image,cv.COLOR_BGR2LAB)
cv.imshow("Lab",lab)

# BGR to RGB
rgb = cv.cvtColor(resized_image,cv.COLOR_BGR2RGB)
cv.imshow("Rgb",rgb)

cv.waitKey(0)