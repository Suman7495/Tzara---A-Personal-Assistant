"""
The core of the Intelligent Personal Assistant

Finds keywords in the input sentence,
then calls the appropriate functions.
"""

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from Speech import speak
from files import open_folder
import firefox
from playmovie import fn_movie, fn_close_movie
from songs import fn_play_song, fn_close_song
from pdf import fn_open_pdf, fn_close_pdf
import os
import time, datetime
import reminder
import terminal
from converse import converse
from confirm import confirm

def tzara(string):
    """
    Searches the input string for keywords, or commands.
    If keywords are found, it calls appropriate function.
    List of functions:
    (1) Open (website, pdf, folder, terminal, reminder)
    (2) Play (movies, songs)
    (3) Tell the time.
    (4) Google, or search for a string online.
    (5) Close (tab, song, movie, pdf)
    (6) Mail (read, send)
    (7) Shutdown
    (8) Reminder
    """
    #Splitting each sentence in a list of words.
    word_list = word_tokenize(string)

    #Setting up stop_words: words that are redundant.
    stop_words = set(stopwords.words('english'))

    #Creating space for a list of sentences without stop_words.
    if "search" not in word_list and "google" not in word_list:
        filtered_sentence = [w for w in word_list if not w in stop_words]
    else:
		filtered_sentence = [w for w in word_list]
   
    if 'open' in filtered_sentence:
        #OPEN WEBSITE
        if 'site' in filtered_sentence:
            print "in function"
            filtered_sentence = [w for w in filtered_sentence \
                if w != "called" and w != "named"]
            firefox.fn_open_site( \
                filtered_sentence[filtered_sentence.index('site') + 1])
        elif 'website' in filtered_sentence and \
            filtered_sentence.index('open') \
                < filtered_sentence.index('website'):
            firefox.fn_open_site( \
                filtered_sentence[filtered_sentence.index('website') + 1])

        #OPEN PDF
        elif 'pdf' in filtered_sentence and \
            filtered_sentence.index('open') \
                < filtered_sentence.index('pdf'):
            filtered_sentence = \
                [w for w in filtered_sentence \
                    if w != "called" and w != "named"]
            fn_open_pdf(filtered_sentence[filtered_sentence.index('pdf') + 1])

        #OPEN FOLDER
        elif 'folder' in filtered_sentence and \
            filtered_sentence.index('open') \
                < filtered_sentence.index('folder'):
            if "called" in string:
                pos = string.index("called") + 7
                string = string[pos:]
            elif "named" in string:
                pos = string.index("named") + 6
                string = string[pos:]
            else:
                pos = string.index("folder")+7
                string = string[pos:]
            open_folder(string)

       #OPEN TERMINAL
        elif 'terminal' in filtered_sentence and \
            filtered_sentence.index('open') \
            < filtered_sentence.index('terminal'):
            terminal.terminal()

        #OPEN REMINDER
        elif 'reminder' in filtered_sentence:
            reminder.reminder()

        elif len(filtered_sentence) > 1:
            sites_path = os.getcwd() + "/Text_Files/comn_sites.txt"
            f_sites = open(sites_path, "r")     
            for line in f_sites:
                name_list = line.strip().split("-")
                #if (n.lower()==''.join(name_list[0:1]).lower()):
                #    counter=1
                #    email_id=''.join(name_list[1:2])
                pos = filtered_sentence.index('open')+1
                if ''.join(filtered_sentence[pos]).lower() \
                    in ''.join(name_list[0:1]).lower():
                    print ''.join(name_list[1:2])
                    firefox.fn_open_site(''.join(name_list[1:2]))
            f_sites.close()

        else:
            speak("You want me to open something,"
                "but I'm not sure what. Could you please repeat?")

    elif 'terminal' in filtered_sentence:
        speak("Would you like me to open the terminal for you?")
        reply = raw_input('\033[1m'+'Username: '+'\033[0m') #modify
        if confirm(reply) == 1:
            terminal.terminal()
        else:
            speak("As you wish.")

    elif 'movie' in filtered_sentence:
        #PLAY MOVIE
        filtered_sentence = [w for w in filtered_sentence \
            if w != "called" and w != "named" and w != "titled"]
        pos = filtered_sentence.index('movie') + 1
        fn_movie(filtered_sentence[pos])

        #PLAY SONG
    elif 'song' in filtered_sentence and filtered_sentence.index('play') \
        < filtered_sentence.index('song'):
        filtered_sentence = [w for w in filtered_sentence \
            if w != "called" and w != "named" and w != "titled"]
        pos = filtered_sentence.index('song') + 1
        fn_play_song(filtered_sentence[pos])

    elif 'time' in filtered_sentence:
        speak(time.strftime("%A") + " " \
            + str(datetime.datetime.now())[:16])

    elif 'google' in filtered_sentence:
        if len(filtered_sentence) > 1:
            pos = filtered_sentence.index('google') + 1
            if 'word' in filtered_sentence \
                and filtered_sentence[-1] != 'word':
                filtered_sentence = \
                    [w for w in filtered_sentence if w != "word"]

            search_string = ''.join(filtered_sentence[pos:])
            firefox.fn_search(search_string)
        else:
            speak("If you want me to open google, say 'open google'")
            speak("If you want me to search for a word,"
                "say 'google <word>'")

    elif 'search' in filtered_sentence:
        if filtered_sentence[-1] == "search":
            speak("Enter the word you would like me to search.")
            search_string = raw_input('\033[1m' + 'Username: ' + '\033[0m')     #modify
            firefox.fn_search(search_string)
            return
        pos = filtered_sentence.index('search') + 1
        search_string = " ".join(filtered_sentence[pos:])
        firefox.fn_search(search_string)

    elif 'reminder' in filtered_sentence:
        speak("Opening reminder")
        reminder.reminder()

    elif 'close' in filtered_sentence:
        if 'tab' in filtered_sentence:
            firefox.fn_close_tab()
            speak('There you go!')
        if 'song' in filtered_sentence:
            fn_close_song()
        if 'movie' in filtered_sentence:
            fn_close_movie()
        if 'pdf' in filtered_sentence:
            fn_close_pdf()
        else:
            speak("I figure you want me to close something,"
                "but I'm not sure what!")

    elif 'ping' in filtered_sentence:
        firefox.ping()

    elif 'mail' in filtered_sentence:
        if 'read' in filtered_sentence or \
            'unread' in filtered_sentence or \
            'check' in filtered_sentence or \
            'see' in filtered_sentence:
            firefox.fn_read_mail()
        elif filtered_sentence[-1] != 'mail':
            pos = filtered_sentence.index('mail') + 1
            firefox.fn_write_mail(filtered_sentence[pos])
        elif filtered_sentence[-1] == 'mail':
            speak("Whom would you like to mail?")
            reply = raw_input('\033[1m' + 'Username: ' + '\033[0m') #modify
            firefox.fn_write_mail(reply)
        else:
            speak("Do you want to mail somebody?"
                " Then type: 'mail person's_name'")
            speak("Or do you want to read your emails?"
                "Then simply type: 'read mail'")

    elif 'shutdown' in filtered_sentence:
        speak("Would you like me to shutdown the system?")
        reply = raw_input('\033[1m' + 'Username: ' + '\033[0m')     #modify
        if confirm(reply) == 1:
            speak("Shutting down system now. Goodbye!")
            os.system("sudo shutdown -h now")
        else:
            speak("As you wish.")

    else:
        speak(converse(string))
    return None
