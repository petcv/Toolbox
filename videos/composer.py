import cv2 as cv
import utils.file_helper as fh

fps = 6
width = 771
height = 1080

print("processing....")

videoWriter = cv.VideoWriter("result/result.mp4", cv.VideoWriter_fourcc(*"XVID"), fps, (width, height))

directory = "resource/ahjk/"
files = fh.getFiles(directory)

for file in files:
    image = cv.imread(directory + file + ".jpg")
    image = cv.resize(image, (width, height))
    for j in range(0, 3):
        videoWriter.write(image)

    cv.imshow("foo", image)
    cv.waitKey(10)

videoWriter.release()

print("done!")