import cv2 as cv
from rescaleMethod import rescaleFrame

capture = cv.VideoCapture("Assets/Videos/person_walking.mp4")

while True:
    isTrue,frame = capture.read()
    if isTrue:
        resized_frame = rescaleFrame(frame,scale=0.25)
        cv.imshow("Resized Video",resized_frame)

    if cv.waitKey(20) & 0xFF==ord('e'):
        break

capture.release()
cv.destroyAllWindows()
