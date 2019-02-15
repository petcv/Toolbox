import cv2 as cv
import re

def visualize(fileName, path):
    fullName = path + fileName
    image = cv.imread(fullName + ".jpg")
    width = image.cols
    height = image.rows

    info = open(fileName + ".txt")
    lines = info.readlines()
    for line in lines:
        vertices = getVertices(line, width, height)
        cv.rectangle(image, {vertices[2], vertices[0]}, {vertices[3], vertices[1]}, {0, 0, 255}, 1, 1, 0)

    #cv.putText(image)
    print(fileName)
    cv.imshow("foo", image)
    cv.waitKey(0)

    info.close()

def getVertices(line, imageWidth, imageHeight):
    match = re.match(r'^(\\d) ([\\d\\.]+) ([\\d\\.]+) ([\\d\\.]+) ([\\d\\.]+)$', line)
    centerX = match.group[2]
    centerY = match.group[3]
    width = match.group[4]
    height = match.group[5]
