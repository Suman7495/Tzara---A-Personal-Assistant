"""
Gets confirmation.

"""
import os
def confirm(reply):
    """
    Checks if reply is in confirmation list.
    If yes, success.
    Else, failure.
    """
    path = os.getcwd() + "Text_Files/confirmations.txt"
    f_ok = open(path, "r")    
    confirmation_list = f_ok.read().strip().split()
    f_ok.close()
    return reply.lower() in confirmation_list
