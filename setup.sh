#!/bin/bash

if [[ ! $(pwd) =~ .*home-server ]]; then
    echo "Please run from the root home-server directory"
    exit 1
fi

sudo apt-get update
sudo apt-get upgrade

echo "Installing dependencies..."
sudo apt-get install build-essential python-dev python-pip
sudo apt-get install nginx
sudo pip install virtualenv

echo "Setting up virtualenv..."
cd server
virtualenv env --no-site-packages
source env/bin/activate
pip install -r ../scripts/requirements.txt

deactivate

echo "Setting up nginx..."
sudo cp scripts/home.nginx /etc/nginx/sites-available/home
sudo rm /etc/nginx/sites-*/default
sudo ln -s /etc/nginx/sites-available/home /etc/nginx/sites-enabled/home

echo "Setting up supervisord..."
sudo cp scripts/supervisord.conf /etc/supervisor/supervisord.conf

echo "Done! Run \"supervisord\" to launch the server as a daemon"
