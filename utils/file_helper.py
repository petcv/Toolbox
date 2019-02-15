import os
from functools import reduce

def getFiles(rootDir):
    result = []

    for fileName in os.listdir(rootDir):
        if os.path.isfile(os.path.join(rootDir, fileName)):
            result.append(fileName)

    result = map(lambda x: os.path.splitext(x)[0], result)
    result = reduce(lambda x, y: x if y in x else x + [y], result, [])

    return result
