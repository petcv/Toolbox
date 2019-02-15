import cv2 as cv
import imageio as ii

print('processing....')

buff = []
for i in range(4, 25):
    fileSuffix = "%02d" % i
    print(fileSuffix)
    image = cv.imread("result/result_{}.jpg".format(fileSuffix))
    image = cv.resize(image, (800, 900))
    image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    buff.append(image)

gif = ii.mimsave('result/result.gif', buff, 'GIF', duration=1)

print('done!')