from moviepy.editor import *

######input###### 



#original video date 
# "/" cannot be used due to location errors
date = ""
#artist name 
artistName = ""
#video ending time
endTime = ""
# original video path
originalVideo = ".mp4"
# save path location 
savePathLoc = ""
#constructed comment input (song and time splitted with row, space between the time and the song name)
inputString = """"""
# resolution height ///// such as (480, 720, 1080) default 720
res = 720



#################

tempArray = inputString.splitlines()
songName = []
startTime = []

j=0
for j in range (0, len(tempArray)):
    splittedTempArray = tempArray[j].split(" ", 1)
    startTime.append(splittedTempArray[0])
    songName.append(splittedTempArray[1])
startTime.append(endTime)

i=0
for i in range (0, len(songName)):
    # save path
    savePath = savePathLoc + songName[i] + " " + artistName + " " + date + ".mp4"
    #time to secs coversion [start]
    v = startTime[i].split(':')
    if len(v) == 1:
        sec = int(v[0])
    if len(v) == 2:
        sec = int(v[0]) * 60 + int(v[1])
    if len(v) == 3:
        sec = int(v[0]) * 3600 + int(v[1]) * 60 + int(v[2])
    #time to secs [end]
    v2 = startTime[i+1].split(':')
    if len(v2) == 1:
        sec2 = int(v2[0])
    if len(v2) == 2:
        sec2 = int(v2[0]) * 60 + int(v2[1])
    if len(v2) == 3:
        sec2 = int(v2[0]) * 3600 + int(v2[1]) * 60 + int(v2[2])

    # edit video
    video = VideoFileClip(originalVideo).subclip(int(sec)-1, int(sec2)-1)

    clip_resized = video.resize(height=res) 
    
    # fps and save
    clip_resized.write_videofile(savePath, fps=29, audio_codec="aac")
