"""
Gets confirmation.

"""
def confirm(reply):
    """
    Checks if reply is in confirmation list.
    If yes, success.
    Else, failure.
    """
    f_ok = open("path/to/file/confirmations.txt", "r")    #modify
    confirmation_list = f_ok.read().strip().split()
    f_ok.close()
    return reply.lower() in confirmation_list
