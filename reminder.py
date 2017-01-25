from Speech import speak
"""
A REMINDER.

Functions: Set, Read, Delete.
Possible amelioration: 
	1. GUI
	2. In delete function, deletes ALL reminders of a given date without asking.
	
"""
def reminder ():
	speak("You want to: set a new reminder, read reminder, or delete reminder? Type 'q' to quit.")
	speak("Input Set or Read or Delete or q.")
	INPUT = (raw_input('\033[1m'+'Suman: '+'\033[0m')).lower()
	#INPUT=INPUT.lower()
	
	while (verify_input(INPUT)== False):
		speak("Input Set or Read or Delete or q.")
		INPUT = (raw_input('\033[1m'+'Suman: '+'\033[0m')).lower()
	
	if (INPUT=="set"):
		set_rm()		
	elif (INPUT=='read'):
		read_rm()		
	elif(INPUT=='delete'):
		delete_rm()	
	else:
		return

def delete_rm():
	speak("Here are the reminders:")
	f=open("/media/suman/New Volume1/Artificial Intelligence/Personal Assistant/Personal Assistant/Text_files/reminder.txt", "r+")
	data=[]
	for line in f:
		print line
		data.append(line)
	raw_input()
	speak('Please enter the date of the reminder in the following format: ')
	print "dd/mm/yyyy"
	reminder_date = raw_input('\033[1m'+'Suman: '+'\033[0m')
	while (verify_date(reminder_date)==False):
		speak("Sorry, invalid input. Try again")
		reminder_date = raw_input('\033[1m'+'Suman: '+'\033[0m')
	
	new_data=[]
	for line in data:
		if (reminder_date in line):
			continue
		new_data.append(line)
	f.seek(0)
	f.writelines([line for line in new_data])			
	f.truncate()
	f.close()


def set_rm():
	speak("Please enter the date of the reminder in the following format: ")
	print "dd/mm/yyyy"
	reminder_date = raw_input('\033[1m'+'Suman: '+'\033[0m')
	
	while (verify_date(reminder_date)==False):
		speak("Sorry, invalid input. Try again")
		reminder_date = raw_input('\033[1m'+'Suman: '+'\033[0m')
	speak("Now set the reminder.")
	reminder_text = raw_input('\033[1m'+'Suman: '+'\033[0m')
	with open("/media/suman/New Volume1/Artificial Intelligence/Personal Assistant/Personal Assistant/Text_files/reminder.txt", "a") as f_reminder:
		f_reminder.write(reminder_date+" - "+reminder_text+"\n")
	f_reminder.close()
	
	speak("Reminder successfully set.")

def read_rm():
	f=open("/media/suman/New Volume1/Artificial Intelligence/Personal Assistant/Personal Assistant/Text_files/reminder.txt", "r")
	for line in f:
		print line
	f.close()
	
def verify_input(input_str):
	acceptable_input=['set','read','delete','q']
	return (input_str in acceptable_input)	
	
def verify_date(input_str):
	if (len(input_str)!=10):
		return False
	if (input_str[2]!="/") or  (input_str[5]!="/"):
		return False 
	checks=0
	for i in xrange(1, 32):
		if (i>=10):
			if (str(i)==input_str[:2]) :
				checks=1
				break
		else:
			if (('0'+str(i))==input_str[:2]):
				checks=1
				break
	
	if (checks==0):
		return False
		
	for i in xrange(1, 13):
		if (i>=10):
			if (str(i)==input_str[3:5]) :
				checks=2
				break
		else:
			if (('0'+str(i))==input_str[3:5]):
				checks=2
				break
				
	if (checks==1):
		return False
	
	for i in xrange(2016, 3000):
		if (str(i)==input_str[-4:]) :
			checks=3
			break
	if (checks==2):
		return False
				
	
