#!/usr/bin/env bash
<<<<<<< HEAD
# Script to set up web servers for the deployment of web_static
sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
sudo echo "<html>
  <head>
  </head>
  <body>
    Local Store
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

=======
# Deploy code
if ! dpkg -l | grep -qE "^ii\s+nginx\s"
then
    sudo apt-get -y update
    sudo apt-get -y install nginx
fi
sudo mkdir -p "/data/web_static/releases/test/"
sudo mkdir -p "/data/web_static/shared/"
content="<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"
sudo touch "/data/web_static/releases/test/index.html"
sudo echo "$content" | sudo tee "/data/web_static/releases/test/index.html" > "/dev/null"
sudo ln -sf "/data/web_static/releases/test/" "/data/web_static/current"
sudo chown -R ubuntu:ubuntu "/data/"
sudo sed -i "47s|^|\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}|" "/etc/nginx/sites-available/default"
>>>>>>> 1d44300a10d128a1aafbdf394eccb58cbbcdede2
sudo service nginx restart
