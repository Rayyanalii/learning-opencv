import cv2 as cv

def rescaleFrame(frame:cv.Mat,scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension  = (width,height)

    return cv.resize(frame, dsize=dimension, interpolation=cv.INTER_AREA)