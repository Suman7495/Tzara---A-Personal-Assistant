"""
Plays a song.
"""
from Speech import speak
import os

def fn_play_song(name):
    """
    Plays the given song with Audacious
    """
    os.system('find /media/suman/New\ Volume1/songs -iname "*'+name+'*"'
        '-exec audacious {} + &disown\;')

def fn_close_song():
    """
    Kills Audacious.
    """
    os.system("killall audacious")
    speak("Song stopped.")
