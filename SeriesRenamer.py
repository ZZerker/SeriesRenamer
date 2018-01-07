from os import listdir
from os.path import isfile, join
from shutil import move

videoExtensions = ["avi", "mkv", "mp4"]
path = join("D:\\","inc","Naruto_Shippuuden")
destinationPath = join("D:\\","Serien")
onlyfiles = [f for f in listdir(path)if isfile(join(path, f))]
seriesName= "Naruto Shippuuden"
for strfile in onlyfiles:
    splitFile = strfile.split(".")
    if len(splitFile) >= 2:
        extension = splitFile[len(splitFile)-1]
        if extension in videoExtensions:
            print("valid File: " + strfile)
            episodeNumber = ""
            fristDigitInName = False
            prevLetterDigit = True
            for letter in strfile:
                if letter.isdigit():
                    fristDigitInName = True
                    if prevLetterDigit:                      
                        episodeNumber += letter                        
                elif fristDigitInName:
                    prevLetterDigit = False
                
            print("moving Episode "+episodeNumber)
            move(join(path,strfile),join(destinationPath,seriesName+" "+episodeNumber+".mp4"))
            
            
        
            



