# Tzara---A-Personal-Assistant

A Personal Assistant name Tzara which helps in daily tasks written in Python2.

Tasks:

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

11. Tell the time and date

12. Shutdown the system

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Requirements

Debian or Ubuntu based system.

An Internet connection is recommended.

### Prerequisites

Setting up the environment.

1) Python 2.7 - Installation instructions can be found [here.](https://www.python.org/downloads/)

2) Pip
```
sudo apt-get update
sudo apt-get install python-pip
``` 
You could also install Pip following [these instructions.](https://pip.pypa.io/en/stable/installing/)

3) gTTS
```
sudo pip install gTTS
```

4) mpg123
```
sudo apt-get install mpg123
```

5) NLTK package
```
sudo pip install -U nltk
```
Or follow [these instructions.](http://www.nltk.org/install.html). 

6) Firefox
```
sudo apt-get install firefox
```

7) Audacious music Player
```
sudo apt-get install audacious
```

8) xdotool
```
sudo apt-get install xdotool
```

9) wmctrl
```
sudo apt-get install wmctrl
```

10) Guake dropdown terminal
```
sudo apt-get install guake
```

### Installing

1) Setting up pathnames:

After having downloaded all files, open EACH ONE and modify according to the instructions provided in the file. 

For example, you may find:
```
f_reminder = open("/path/to/the/file/reminder.txt", "r+")
```
Replace "/path/to/the/file" with the actual pathname to the file called "reminder.txt". 

Thus, in my system, this particular pathname was:
```
f_reminder = open("/media/suman/New Volume1/Artificial Intelligence/Personal Assistant/Text_files/reminder.txt", "r+")
```

This will ensure the Personal Assistant is customised only to you.

2) Emails:

This is particular for Gmail accounts. 

To send emails and read emails, you will need access to your Gmail account. But Gmail will block your email if you don't get a password, as it doesn't recognise the application. 

To obtain a password for Tzara, follow [these instructions.](https://support.google.com/accounts/answer/6010255?hl=en)

Then, open a plain text document in the Home Directory.

Copy paste the following code. 
```
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

3) Setting up .txt files:

You can modify the following .txt files to personalise Tzara further:

a) bye.txt - Add ways for Tzara to say goodbye.

b) comn_sites.txt - List of the sites you visit.

c) confirmations.txt - Add ways for to confirm.

d) corporat.txt - List of corpora from where Tzara develops her sentences. Currently from Brown Corpus

e) email_id.txt - List of email-ids. E.g. john@gmail.com - Simply say: "Mail John", and Tzara will mail john@gmail.com

f) folder.txt - List of folder names and paths you frequently use. E.g. Suppose you go to /home/username/Documents often. Simply add "Documents - /home/username/Documents" to folder.txt, and then you can simply tell Tzara: "Open folder documents", and she will open the correct folder.

g) greetings.txt - Ways Tzara will greet you.

## Running the tests



### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc

