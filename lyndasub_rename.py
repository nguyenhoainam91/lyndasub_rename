#
#   Author: zgezt
#   Date:   15.12.2015
#   Des:    This is a tool to copy and rename subtitle 
#           file you download from www.lyndasub.ir
#           to same folder with your video you download 
#           from www.lynda.com (with IDM)
#           I just hate to press F2 many times.

#   Step:

#       1. Download video from www.lynda.com with IDM
#       2. Extract and rename the file (.zip) you have downloaded from www.lyndasub.ir to 'lyndasub'
#       3. Run it with Python 3
#
#       Example:
#       D:\
#       |_ Foundations of Programming Design Patterns
#           |_ lyndasub_rename.py    <=====
#           |_ 135365_00_01_WX30_welcome.mp4
#           |_ 135365_00_02_XR15_whatyoushouldknow.mp4
#           |_ lyndasub
#               |_ 00. Introduction
#                   |_ 01. Welcome.srt
#                   |_ 02. What you should know before watching this course.srt
#
#



import os
import shutil


print(os.getcwd())

LYNDASUB_FOLDER = "lyndasub"
VIDEOS_FILE_EXTENSION = ".mp4"

if not os.path.exists(LYNDASUB_FOLDER):
    print("ERROR: Please extract and rename the folder you have downloaded from www.lyndasub.ir to 'lyndasub' !")
else:
    all_files = os.listdir(".")
    all_chapter = os.listdir(LYNDASUB_FOLDER)
    for video_name in all_files:
        if (os.path.splitext(video_name)[1] == VIDEOS_FILE_EXTENSION):
            video_name_split = video_name.split("_")
            chapter_num = video_name_split[1]
            lesson_num = video_name_split[2]
            
            for chapter_name in all_chapter:
                if chapter_name.startswith(chapter_num):
                    for lesson_name in os.listdir(os.path.join(LYNDASUB_FOLDER,chapter_name)):
                        if lesson_name.startswith(lesson_num):
                            path_of_subtile = os.path.join(LYNDASUB_FOLDER, chapter_name, lesson_name)
                            shutil.copy(path_of_subtile, ".")
                            os.rename(lesson_name, os.path.splitext(video_name)[0] + ".srt")
                            print("Add sub for " + video_name)
                            

print("Press Enter to exit.")
input()
