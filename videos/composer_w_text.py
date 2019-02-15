import cv2 as cv
import numpy as np
from PIL import Image, ImageDraw, ImageFont

fps = 24
width = 1920
height = 1080

def getProcessedImage(image, values):
    img = Image.fromarray(image)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("simsun.ttc", 24)
    # 1: 50, 2: 30, 3: 30, 4: 100, 5: 10, 6: 10

    draw.text((490, 238), values[2], fill=(255, 255, 255), font=font)
    draw.text((485, 304), format(float(values[2])/30, "0.2f"), fill=(255, 255, 255), font=font)
    draw.text((1480, 242), values[3], fill=(255, 255, 255), font=font)
    draw.text((1475, 308), format(float(values[3])/100, "0.2f"), fill=(255, 255, 255), font=font)
    draw.text((490, 525), values[4], fill=(255, 255, 255), font=font)
    draw.text((485, 593), format(float(values[4])/10, "0.2f"), fill=(255, 255, 255), font=font)
    draw.text((1480, 525), values[5], fill=(255, 255, 255), font=font)
    draw.text((1475, 595), format(float(values[5])/10, "0.2f"), fill=(255, 255, 255), font=font)
    draw.text((490, 807), values[0], fill=(255, 255, 255), font=font)
    draw.text((485, 875), format(float(values[0])/50, "0.2f"), fill=(255, 255, 255), font=font)
    draw.text((1480, 807), values[1], fill=(255, 255, 255), font=font)
    draw.text((1475, 877), format(float(values[1])/30, "0.2f"), fill=(255, 255, 255), font=font)
    
    return np.asarray(img)

print("processing....")

videoWriter = cv.VideoWriter("result/result.avi", cv.VideoWriter_fourcc(*"XVID"), fps, (width, height))
video = cv.VideoCapture("resource/bjdt.mp4")

success,frame = video.read()
f = []
l = []
for i in range(0, 6):
    f.append(open("resource/passenger_count/" + str(i+1) + ".txt"))
    l.append(f[i].readline())

i = 1
while success:
    image = getProcessedImage(frame, l)

    cv.imshow("foo", image)
    cv.waitKey(10)

    videoWriter.write(image)
    success,frame = video.read()
    for i in range(0, 6):
        l[i] = f[i].readline()

    i = i + 1
    print(i)

for i in range(0, 6):
    f[i].close()

videoWriter.release()
video.release()
print("done!")