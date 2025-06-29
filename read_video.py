import cv2 as cv

capture = cv.VideoCapture("Assets/Videos/person_walking.mp4")

while True:
    isTrue,frame = capture.read()
    if isTrue:
        cv.imshow("Video",frame)

    if cv.waitKey(20) & 0xFF==ord('e'):
        break

capture.release()
cv.destroyAllWindows()
