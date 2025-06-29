import cv2 as cv
import numpy as np

def translate(frame:cv.Mat,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (frame.shape[1],frame.shape[0])
    return cv.warpAffine(frame,transMat,dimensions)

def rescaleFrame(frame:cv.Mat,scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension  = (width,height)

    return cv.resize(frame, dsize=dimension, interpolation=cv.INTER_AREA)

def rotateFrame(frame:cv.Mat,angle,rotationPoint=None):
    (height,width) = frame.shape[:2]

    if rotationPoint is None:
        rotationPoint = (width//2,height//2)
    
    rotMat = cv.getRotationMatrix2D(rotationPoint,angle,1)
    dimensions = (width,height)

    return cv.warpAffine(frame,rotMat,dimensions)
