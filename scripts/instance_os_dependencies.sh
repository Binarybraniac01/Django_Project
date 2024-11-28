#!/usr/bin/env bash

sudo apt update
# Install Python3 pip
sudo apt install -y python3-pip

# Install Nginx
sudo apt install -y nginx

# Install Virtualenv
sudo apt install -y virtualenv

# Install additional dependencies
sudo apt-get install -y default-libmysqlclient-dev build-essential pkg-config
