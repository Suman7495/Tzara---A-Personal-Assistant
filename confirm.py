"""
Gets confirmation.

Modify: 
12: f_ok = open("path/to/file/confirmations.txt", "r")
"""
def confirm(reply):
    """
    Checks if reply is in confirmation list.
    If yes, success.
    Else, failure.
    """
    f_ok = open("path/to/file/confirmations.txt", "r")
    confirmation_list = f_ok.read().strip().split()
    f_ok.close()
    return reply.lower() in confirmation_list
