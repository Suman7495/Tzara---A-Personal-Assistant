"""
Gets confirmation
"""
def confirm(reply):
    """
    Checks if reply is in confirmation list.
    If yes, success.
    Else, failure.
    """
    f_ok = open("/media/suman/New Volume1/Artificial Intelligence"
        "/Personal Assistant/Personal Assistant/Text_files"
        "/confirmations.txt", "r")
    confirmation_list = f_ok.read().strip().split()
    f_ok.close()
    return reply.lower() in confirmation_list
