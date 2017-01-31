"""
Plays a movie
"""
from Speech import speak
import os

def fn_movie(name):
    """
    Searches for the movie name in 2 paths.

    If movie is found, plays with vlc.
    """
    path_list = ["/path1/", "/path2"
        "/path3/"]                          #modify
    for path in path_list:
        os.system('find '+ path + ' -iname "*' + name + '*"'
            ' -exec vlc --fullscreen {} + & >/dev/null;')
    os.system("clear")
    speak("Hope you enjoy the movie!!!")
    os.system("clear")

def fn_close_movie():
    """
    Kills vlc
    """
    os.system("killall vlc")
    speak("Job's done.")

