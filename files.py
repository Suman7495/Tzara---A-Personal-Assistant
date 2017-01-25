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
    f_fldr = open("/path/to/the/file/folder.txt", "r")    #modify
    for line in f_fldr:
        name_list = line.strip().split("-")
        if name.lower() == ''.join(name_list[0:1]).lower():
            counter = 1
            path = ''.join(name_list[1:2])
            os.system('xdg-open ' + path)
            speak("Opened the requested folder.")
            break
    f_fldr.close()
    if counter == 0:
        speak("Sorry, but I could not find the folder.")
