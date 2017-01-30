"""
Several modules using firefox browser.

Tasks:
(1) Checks for an Internet connection.
(2) Searches (Google) for a word.
(3) Send emails.
(4) Reads unread mails.
(5) Opens any website.
(6) Closes a tab.
"""
from Speech import speak
from confirm import confirm
import os

def ping():
    """
    Checks for an Internet connection.
    If success, saves "success" in the file mentioned below.
    Else, saves "failure".
    """
    path = os.getcwd() + "/Text_Files/ping_result.txt"
    path_os = path.replace(" ", "\ ")
    path_os = path_os.replace("(", "\(")
    path_os = path_os.replace(")", "\)")
    os.system('guake -n CUR_DIR -e "if ! ping -c 1 '
        'www.google.com &>/dev/null;'
        'then echo fail >' + path_os + ';'   
        'else echo success>'+ path_os + ';fi;clear"')    
    os.system("guake -s 1")
    os.system("guake -s 2 -e exit")

    f_ping = open(path)    
    result = f_ping.read().strip().split("\n")
    result = ''.join(result)
    f_ping.close()
    if result == 'success':
        return 1
    else:
        speak("Sorry. Internet is down currently.")
        return 0

def fn_search(word):
    """
    Calls ping().
    If success:
        Searches for the given sentence.
    """
    
    if ping() == 0:
        return
    speak('Would you like me to search for "' + word + '"?')
    reply = raw_input('\033[1m' + 'Username: ' + '\033[0m')    #modify: Change "Username"
    if confirm(reply) == 1:
        word = word.replace(" ", "+")
        search_link = "www.google.co.in/#q=" + word
        speak('Cool. Here are the results.')
        os.system('guake -n CUR_DIR -e "firefox "' + search_link +
            '" & >/dev/null"')
        os.system("guake -s 1")
        os.system("guake -s 2 -e exit")
        return
    else:
        speak("As you wish.")
        return

def fn_close_tab():
    """
    Closes a firefox tab.
    """
    speak('Do you want me to close the current tab?')
    reply = raw_input('\033[1m' + 'Username: ' + '\033[0m')	#modify: Change "Username"
    if confirm(reply) == 1:
        os.system('wmctrl -a firefox; xdotool key Ctrl+w;')
    else:
        speak('Ok')
        return

def fn_open_site(site):
    """
    Opens a website on the firefox browswer.
    """
    if ping() == 0:
        speak("Sorry. Internet is down currently.")
        return
    if site.endswith(".com") == True:
        os.system('guake -n CUR_DIR -e "firefox "'+ site +
            '" & >/dev/null"')
        speak("Please give me a while to complete the task.")
        os.system("guake -s 1")
        os.system("guake -s 2 -e exit")
        speak("Task successfully completed.")

    else:
        os.system('guake -n CUR_DIR -e "firefox "' + site +
            '".com & >/dev/null"')
        speak("Please give me a while.")
        os.system("guake -s 1")
        os.system("guake -s 2 -e exit")
        speak("Task successfully completed.")


def fn_write_mail(name):
    """
    If an Internet connection is there:
        Checks if the given name exists in directory.
        If it does, asks user to write the mail, then send.
        Else, asks for a valid email-id. Then asks the user to write.
    Else quits.
    """
    if ping() == 0:
        speak("Sorry. The Internet is down currently.")
        return
    counter = 0
    email_path = os.getcwd() + "/Text_Files/email_id.txt"
    f_email = open(email_path)	
    for line in f_email:
        print line
        name_list = line.strip().split("-")
        if name.lower() == ''.join(name_list[0:1]).lower():
            counter = 1
            email_id = ''.join(name_list[1:2])
            speak("Now write the mail. Press Control+D when you are done.")
            os.system('mail ' + email_id)
            speak("The mail has been sent.")
            break
    f_email.close()
    if counter == 0:
        speak("Sorry. The name doesn't exist in the directory."
            "You'll have to give me the person's email address"
            " for me to mail him. Would you like to do that?")
        reply = raw_input('\033[1m' + 'Username: ' + '\033[0m')		#modify: Change "Username"
        if confirm(reply) == 1:
            speak("Ok. Now please enter a valid email address.")
            email_id = raw_input('\033[1m' + 'Username: ' + '\033[0m')	#modify: Change "Username"
            speak("Now write the mail. "
            "Press Control+D when you are done.")
            os.system('mail ' + email_id)
            speak("The mail has been sent.")

        else:
            speak("As you wish.")

def fn_read_mail():
    """
    Checks how many unread mails are there in the inbox.
    """
    if ping() == 0:
        speak("Sorry. The Internet is down currently.")
        return
    os.system("/path/to/the/file/check_email.sh")		#modify
    inbox_path = os.getcwd() + "/Text_Files/inbox_details.txt"
    f_inbx = open(inbox_path)	
    data = f_inbx.read()
    f_inbx.close()
    unread_mails = int(data[(data.index("<fullcount>") + 11)\
		:data.index("</fullcount>")])
    speak("You have " + str(unread_mails) + " unread mails.")

