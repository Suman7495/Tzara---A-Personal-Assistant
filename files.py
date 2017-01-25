"""
Opens folders
"""

import os
from Speech import speak

def open_folder(name):
    """
    Checks if a folder with the given name exists in directory.
    If yes, opens it.
    """
    name = name.strip()
    #os.system("find -type d -iname '*"+name +"*' -exec xdg-open ")
    counter = 0
    f_fold = open("/media/suman/New Volume1/Artificial Intelligence"
        "/Personal Assistant/Personal Assistant/Text_files/folder.txt", "r")
    for line in f_fold:
        name_list = line.strip().split("-")
        if name.lower() == ''.join(name_list[0:1]).lower():
            counter = 1
            path = ''.join(name_list[1:2])
            os.system('xdg-open ' + path)
            speak("Opened folder.")
            break
    f_fold.close()
    if counter == 0:
        speak("Sorry could not find folder.")
