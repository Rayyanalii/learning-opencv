import cv2 as cv

def detect_face(imageURL:str,image_title:str,haar_cascadeURL:str,scale=1.1,neighbors=3):
    img = cv.imread(imageURL)
    cv.imshow(image_title,img)

    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    cv.imshow("Gray",gray)

    haarCascade = cv.CascadeClassifier(haar_cascadeURL)

    faces_rect = haarCascade.detectMultiScale(gray,scale,neighbors)
    print(f"No. of faces found: {len(faces_rect)}")

    for rectangle in faces_rect:
        (x,y,w,h) = rectangle
        cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

    cv.imshow("Detected Faces",img)
    cv.waitKey(0)

detect_face("Assets/Photos/breaking_bad_group.jpg","Breaking Bad Group","Haar_Cascades/frontal_face.xml",neighbors=15)
