import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype="uint8")
# cv.imshow("Black Canvas",blank)

# Paining entire canvas a color (B,G,R)
# blank[:] = 255,0,0
# cv.imshow("Blue Canvas",blank)

# Paining certain portion of canvas a color (B,G,R)
# blank[100:200,250:300] = 0,0,255
# cv.imshow("Red Canvas",blank)

#Drawing Rectangle
# cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),color=(0,255,0),thickness=-1)
# cv.imshow("Green Rectangle",blank)

#Drawing Circle
# cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),radius=20,color=(0,255,0),thickness=2)
# cv.imshow("Green Rectangle",blank)

#Draw Line
# cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),color=(255,255,255),thickness=2)
# cv.imshow("Line",blank)

#Write Texts
cv.putText(blank,"Hello Ayyan Here",(0,blank.shape[0]//2),cv.FONT_HERSHEY_DUPLEX,fontScale=1,color=(255,255,255),thickness=2)
cv.imshow("Text",blank)


cv.waitKey(0)