import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from utils import rescaleFrame

image = cv.imread("Assets/Photos/red_deer.jpg")
resized_image = rescaleFrame(image,scale=0.25)

cv.imshow("Red Deer",resized_image)

blank = np.zeros(resized_image.shape[:2],dtype="uint8")

mask = cv.circle(blank, (resized_image.shape[1]//2,resized_image.shape[0]//2),100,255,-1)
cv.imshow("Mask",mask)

gray = cv.cvtColor(resized_image,cv.COLOR_BGR2GRAY)
cv.imshow("Grayscale",gray)

masked = cv.bitwise_and(gray,gray,mask=mask)
cv.imshow("Masked",masked)

gray_hist = cv.calcHist([gray],[0],masked,histSize=[256],ranges=[0,256])
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("No. of Pixels")
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()


cv.waitKey(0)