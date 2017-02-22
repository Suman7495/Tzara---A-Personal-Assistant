#!/bin/bash
echo "Initialising setup..."
sudo apt-get update 
sudo apt-get upgrade 
echo "Installing pip..."
sudo apt-get install python-pip

echo "Installing gTTS..."
sudo pip install gTTS

echo "Installing mpg123..."
sudo apt-get install mpg123

echo "Installing NLTK. This may take a few hours..."
sudo pip install -U nltk

echo "Installing Firefox Browser..."
sudo apt-get install firefox

echo "Installing Audacious Music Player..."
sudo apt-get install audacious

echo "Installing xdotool..."
sudo apt-get install xdotool

echo "Installing wmctrl..."
sudo apt-get install wmctrl

echo "Installing Guake Dropdown Terminal..."
sudo apt-get install guake

echo "Installing xdg-utils..."
sudo apt-get install xdg-utils

echo "Setting up .desktop file"

STR="[Desktop Entry]
Encoding=UTF-8
Type=Application
Name=Tzara\n
Comment=A Virtual Personal Assistant
Exec=guake -n guake -t -e 'python /usr/local/lib/python2.7/dist-packages/tzara/main.pyc' guake -r 'Tzara'
Terminal=True
Type=Application
Categories=Application; "
if [ ! -e /usr/share/applications/Tzara.desktop  ]; then
  echo "Setting up .desktop file"
  echo "${STR}" | sudo tee sudo /usr/share/applications/Tzara.desktop > /dev/null
  read -n1 -r -p "Press any key to continue..." key
fi
