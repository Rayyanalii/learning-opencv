import cv2 as cv
from utils import rescaleFrame

capture = cv.VideoCapture("Assets/Videos/Happy_Patient.mp4")

while True:
    isTrue,frame = capture.read()
    if isTrue:
        resized_frame = rescaleFrame(frame,scale=0.25)
        gray = cv.cvtColor(resized_frame,cv.COLOR_BGR2GRAY)

        haarCascade = cv.CascadeClassifier("Haar_Cascades/frontal_face.xml")

        faces_rect = haarCascade.detectMultiScale(gray,1.1,5)
        print(f"No. of faces found: {len(faces_rect)}")
        for rectangle in faces_rect:
            (x,y,w,h) = rectangle
            cv.rectangle(resized_frame,(x,y),(x+w,y+h),(0,255,0),2)
        cv.imshow("Detected Faces",resized_frame)

    if cv.waitKey(20) & 0xFF==ord('e'):
        break

capture.release()
cv.destroyAllWindows()
