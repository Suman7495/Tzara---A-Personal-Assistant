# Tzara---A-Personal-Assistant

A Personal Assistant name Tzara which helps in daily tasks written in Python 2.7.

####Tasks:

1. Send emails

2. Search the internet 

3. Open and close websites

4. Set reminders

5. Play movies and songs

6. Open documents and pdfs

7. Open any application

8. Update the system

9. Open the terminal

10. Converse - basic

11. Tell date and time

12. Shutdown the system

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Requirements

Debian or Ubuntu based system.

An Internet connection is recommended.

## Prerequisites

Environment Setup.

1) Python 2.7 - Installation instructions can be found [here.](https://www.python.org/downloads/)

2) Pip
```bash
sudo apt-get update
sudo apt-get install python-pip
``` 
You could also install Pip following [these instructions.](https://pip.pypa.io/en/stable/installing/)

3) gTTS
```bash
sudo pip install gTTS
```

4) mpg123
```bash
sudo apt-get install mpg123
```

5) NLTK package
```bash
sudo pip install -U nltk
```
Or follow [these instructions.](http://www.nltk.org/install.html)

6) Firefox
```bash
sudo apt-get install firefox
```

7) Audacious music Player
```bash
sudo apt-get install audacious
```

8) xdotool
```bash
sudo apt-get install xdotool
```

9) wmctrl
```bash
sudo apt-get install wmctrl
```

10) Guake dropdown terminal
```bash
sudo apt-get install guake
```

## Installation

####1) Paths setup:

After having downloaded all files, open EACH ONE and modify according to the instructions provided in the file. 

For example, you may find:
```python
f_reminder = open("/path/to/the/file/reminder.txt", "r+")
```
Replace "/path/to/the/file" with the actual pathname to the file called "reminder.txt". 

Thus, in my system, this particular pathname was:
```python
f_reminder = open("/media/suman/New Volume1/Artificial Intelligence/Personal Assistant/Text_files/reminder.txt", "r+")
```

This will ensure the Personal Assistant is customised only to you.

####2) Emails:

This is particular for Gmail accounts. 

To send emails and read emails, you will need access to your Gmail account. But Gmail will block your email if you don't get a password, as it doesn't recognise the application. 

To obtain a password for Tzara, follow [these instructions.](https://support.google.com/accounts/answer/6010255?hl=en)

Then, open a plain text document in the Home Directory.

Copy paste the following code. 
```bash
#!/bin/bash

username=your_email_here"
password="your_password_here"
echo
curl -u $username:$password --silent "https://mail.google.com/mail/feed/atom" > /path/to/the/file/inbox_details.txt
```

Replace "your_email_here" with your email-id. E.g. john@gmail.com

Replace "your_password_here"  with the new password respectively. Note: the password is NOT your general email account password. It is specific to this application.

Replace "/path/to/the/file/" with the pathname to the file "inbox_detail.txt"

Rename the document to: "check_email.sh"

####3) Setting up .txt files:

You can modify the following .txt files to personalise Tzara further:

a) bye.txt - Add ways to say goodbye.

b) comn_sites.txt - Add sites you visit.

c) confirmations.txt - Add ways to confirm.

d) corporat.txt - List of corpora from where Tzara develops her sentences. Currently from Brown Corpus

e) email_id.txt - Add email-ids. E.g. john@gmail.com - Simply say: "Mail John", and Tzara will mail john@gmail.com

f) folder.txt - Add folder names and paths you frequently use. E.g. Suppose you go to /home/username/Documents often. Add "Documents - /home/username/Documents" to "folder.txt", and then you can simply tell Tzara: "Open folder documents", and she will open the correct folder.

g) greetings.txt - Add ways for Tzara to greet you.

## Deployment

1) Open the guake terminal.

2) Input the following code:
```bash
python /path/to/the/file/main.py
```
Replace "/path/to/the/file" to the pathname to the file called "main.py". This file initialises Tzara.

Tzara will greet you with something like: "Hi, my name is Tzara. How may I help you?"

Go on and chat with your newfound friend.

3) To end chat, type anything like:
```
Bye Tzara
```
or 

```
Cya Tzara
```
4) 
## Authors

Suman Pal

