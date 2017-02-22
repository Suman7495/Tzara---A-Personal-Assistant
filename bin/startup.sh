#!/bin/bash
echo "Setting up .desktop file"

STR=$'[Desktop Entry]
Encoding=UTF-8
Type=Application
Name=Tzara
Comment=A Virtual Personal Assistant
Exec=guake -n guake -t -e "python /usr/local/lib/python2.7/dist-packages/tzara/main.pyc" guake -r "Tzara"
Terminal=True
Type=Application
Categories=Application;'
if [ ! -e /usr/share/applications/Tzara.desktop  ]; then
  echo "Setting up .desktop file"
  echo "$STR" | sudo tee sudo /usr/share/applications/Tzara.desktop > /dev/null
  read -n1 -r -p "Press any key to continue..." key
fi
