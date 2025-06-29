import cv2 as cv
from rescaleMethod import rescaleFrame

image = cv.imread("Assets/Photos/red_deer.jpg")
resized_image = rescaleFrame(image,scale=0.25)

cv.imshow("Red Deer",resized_image)

canny = cv.Canny(resized_image,125,175)
cv.imshow("Canny Edges",canny)

# Need structured image to dilate, in this case the canny image
dilate = cv.dilate(canny, (7,7),iterations=2)
cv.imshow("Dilate",dilate)

# Need dilated image to erode back to struturing image
erode = cv.erode(dilate,(7,7),iterations=2)
cv.imshow("Eroded",erode)

cv.waitKey(0)