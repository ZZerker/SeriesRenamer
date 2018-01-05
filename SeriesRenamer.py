from os import listdir
from os.path import isfile, join

print("Test")
videoExtensions = ["avi", "mkv", "mp4"]
mypath = join("D:", "Temp", "TestVideos")
onlyfiles = [f for f in listdir("D:\Temp\TestVideos\\")if isfile(join("D:\Temp\TestVideos\\", f))]

for strfile in onlyfiles:
    splitFile = strfile.split(".")
    if len(splitFile) >= 2:
        extension = splitFile[len(splitFile)-1]
        if extension in videoExtensions:
            print("accepted File: " + strfile)

