from os import listdir
from os.path import isfile, join

videoExtensions = ["avi", "mkv", "mp4"]
mypath = join("D:", "Temp", "TestVideos")
onlyfiles = [f for f in listdir("D:\Temp\TestVideos\\")if isfile(join("D:\Temp\TestVideos\\", f))]

for strfile in onlyfiles:
    splitFile = strfile.split(".")
    if len(splitFile) >= 2:
        extension = splitFile[len(splitFile)-1]
        if extension in videoExtensions:
            print("valid File: " + strfile)
            episodeNumber = ""
            prevLetterDigit = False
            for letter in strfile:
               if letter.isdigit():
                   if !prevLetterDigit:
                       pass
                   episodeNumber+=letter
            
            print(episodeNumber)
            
            
        
            



