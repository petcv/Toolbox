import cv2 as cv
import numpy as np
import utils.file_helper as fh

print('processing....')

directory = "resource/"
files = fh.getFiles(directory)

for file in files:
    video = cv.VideoCapture(directory + file + ".avi")
    success,frame = video.read()
    i = 0
    while success and i < 400:
        outputName = "result/temp/" + str(i) + ".jpg"
        #frame = cv.resize(frame, (640, 360))
        cv.imwrite(outputName, frame)
        success,frame = video.read()
        i = i + 1
        print(i)

    video.release()

print('done!')