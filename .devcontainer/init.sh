#!/bin/bash

sudo apt update
sudo apt install -y qrencode
sudo apt install -y python3-pip
sudo sed -i 's/AllowOverride None/AllowOverride All/' /etc/apache2/conf-enabled/serve-cgi-bin.conf 
sudo a2enmod cgid
sudo service apache2 start
pip install pytest