from utils import file_helper as fh

rootDir = "c:/workspace/resource/training_yolo/"
srcDir = rootDir + "src/"
tarDir = rootDir + "tar/"

files = fh.getFiles(srcDir)

for file in files:
    f = open(file, "r")
    print(file)
    f.close()
