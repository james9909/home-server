#!/bin/bash

MYSQL_ROOT_PASSWORD="i_hate_passwords"

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
sudo bash -c "curl https://raw.githubusercontent.com/Supervisor/initscripts/master/ubuntu > /etc/init.d/supervisord"
sudo chmod +x /etc/init.d/supervisord
sudo update-rc.d supervisord defaults

echo "Creating database..."
mysql -u root -p$MYSQL_ROOT_PASSWORD -e "CREATE DATABASE IF NOT EXISTS home"

echo "Generating secret key..."
dd if=/dev/urandom of=server/.secret_key bs=128 count=1

echo "Done! Run \"supervisord\" to launch the server as a daemon"
