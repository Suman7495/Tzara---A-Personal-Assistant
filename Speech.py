"""
Speaks input string using the internet.
"""
from gtts import gTTS
import os

def speak(out_string):
    """
    Speaks using gTTs from the internet.
    """
    path = os.getcwd() + "/Text_Files/ping_result.txt"
    path_os = path.replace(" ", "\ ")
    path_os = path_os.replace("(", "\(")
    path_os = path_os.replace(")", "\)")
    os.system("if ! ping -c 1 www.google.com>/dev/null;"
        "then echo fail >"+ path_os +";"   
        "else echo success>"+ path_os + ";fi;")
    f_ping = open(path)  
    result = f_ping.read().strip().split("\n")
    f_ping.close()
    print '\033[1m' + 'Tzara: ' + '\033[0m' + out_string
    if result[0] == 'success':
        tts = gTTS(text = out_string, lang = 'en')
        tts.save("hello.mp3")
        os.system("mpg321 -q hello.mp3")


