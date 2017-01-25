"""
Tzara - An Intelligent Personal Assistant.

Main loop.
"""
import time
from tzara import tzara
from Speech import speak
import os
import random
from datetime import datetime
from confirm import confirm
from firefox import ping

def check_last_update():
    """
    Checks when the system was last updated.
    If the system was not updated for the last 2 days, updates system.
    """
    f_update = open("/path/to/file/prev_update.txt", 'r+')  #modify
    prev_date = f_update.read().strip().split("/")
    current_date = time.strftime("%d/%m/%Y")
    date = current_date.strip().split("/")
    if (int(date[0])-int(prev_date[0]) > 2) or \
        (int(date[1])-int(prev_date[1]) > 0) or \
        (int(date[2])-int(prev_date[2]) > 0):
        if ping() == 1:
            speak("Hey, I just realised that it's been a while that " \
                "your system has been updated.")
            speak("Would you like to update system now?")
            reply = raw_input('\033[1m'+'Username: '+'\033[0m') #modify
            if confirm(reply) == 1:
                speak("Please input password to update system.")
                os.system("sudo apt-get update && apt-get upgrade")
                f_update.seek(0)
                f_update.write(current_date)
                f_update.truncate()
                speak("System successfully updated.")
        else:
            speak("It's been a while since your system has been updated. " \
                "I can't update it now, since Internet is down.")
    f_update.close()

def check_reminder():
    """
    Checks if you have any reminder set for today.
    """
    current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    c_year = current_date[0:4]
    c_month = current_date[5:7]
    c_date = current_date[8:10]
    to_del = ''
    f_reminder = open("/path/to/the/file/reminder.txt", "r+")   #modify
    for line in f_reminder:
        r_date = line[0:2]
        if r_date == c_date:
            r_month = line[3:5]
            if r_month == c_month:
                r_year = line[6:10]
                if r_year == c_year:
                    speak("You have a reminder set for today." \
                        "This is what it says: \n" + line[11:])
                    speak("Would you like me to delete the reminder now?")
                    reply = raw_input('\033[1m'+'Username '+'\033[0m')  #modify
                    if confirm(reply) == 1:
                        to_del = line
                        #TO FINISH
    f_reminder.close()

def main():
    """
    Greets the user.
    Checks when the system was last updated.
    Checks if there are reminders.
    Waits for user input.
    If input is "bye" (or similar), quits.
    Else passes the user input to the function tzara() stored in tzara.py
    """
    f_greetings = open("/path/to/the/file/greetings.txt", "r")  #modify
    greetings_list = f_greetings.read().strip().split("\n")
    f_greetings.close()
    random_greeting = random.randrange(0, len(greetings_list))
    speak(greetings_list[random_greeting])

    check_last_update()
    check_reminder()

    f_bye = open("/path/to/the/file/bye.txt", "r")  #modify
    bye_list = f_bye.read().strip().split("\n")
    f_bye.close()
    bye_list2 = [''.join(bye_list[i])+" tzara" for i in range(0, len(bye_list))]
    bye_list3 = [''.join(bye_list[i])+" then" for i in range(0, len(bye_list))]
    while 1:
        input_string = raw_input('\033[1m'+'Suman: '+'\033[0m')
        if input_string:
            input_string = input_string.lower()
            if input_string in bye_list or \
                input_string in bye_list2 or \
                input_string in bye_list3:
                time_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                if int(time_now[11:13]) > 20 or int(time_now[11:13]) < 4:
                    speak("Goodnight.")
                else:
                    speak('See you later then! Have a good day!')
                return
            tzara(input_string)

if __name__ == "__main__":
    main()
