"""
Opens pdf given filename.
"""
from Speech import speak
import os

def fn_open_pdf(name):
    """
    Opens the pdf using evince.
    """
    os.system('find -iname "*' + name +
		'*.pdf" -exec evince {} + &disown\;')
    speak("There you go! Enjoy reading!")

def fn_close_pdf():
    """
    Kills evince.
    """
    speak("Closing PDF.")
    os.system("killall evince")
