from ID3 import *
import os

path1 = input("Input path for folder")

for foldername in os.listdir(path1):
    if foldername == '.DS_Store':
        continue
    else:
        path2 = path1 + foldername
        for filename in os.listdir(path2):
            parsed_title = filename.strip(".mp3").split(" - ")
            if len(parsed_title) == 1:
                continue
            else:
                path3 = path2 + '/' + filename
                id3info = ID3(path3)
                id3info.title = parsed_title[3]
                id3info.artist = parsed_title[2]
                id3info.year = foldername
                id3info.track = parsed_title[1]
                id3info.album = parsed_title[0]
            
