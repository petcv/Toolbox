import cv2 as cv
import numpy as np

fps = 13
width = 733#1920
height = 467#1080

def getProcessedImage(image):
    img = image[66:533, 333:1066]
    
    #rows,cols = image.shape[0:2]
    #if rows != height or cols != width:
    #    image = cv.resize(image, (width, height))
    
    return img

print('processing....')

videoWriter = cv.VideoWriter('C:/Workspace/Repository/YoloTest/videos/tar3.avi', cv.VideoWriter_fourcc(*'XVID'), fps, (width, height))
video = cv.VideoCapture('C:/Workspace/Repository/YoloTest/videos/test.mp4')
success,frame = video.read()
i = 1
while success:
    image = getProcessedImage(frame)
    if i % 2 == 0:
        videoWriter.write(image)
    success,frame = video.read()
    i = i + 1
    print(i)

videoWriter.release()
video.release()
print('done!')