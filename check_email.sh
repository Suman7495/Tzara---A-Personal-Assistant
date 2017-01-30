#!/bin/bash

username = "your_email_here"
password = "your_password_here"
echo
curl -u $username:$password --silent "https://mail.google.com/mail/feed/atom" > /path/to/the/file/inbox_details.txt
