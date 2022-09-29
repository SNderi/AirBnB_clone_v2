#!/usr/bin/env bash
# Sets up the web servers for the deployment of web_static.

REQUIRED_PKG="nginx"
PKG_OK=$(dpkg-query -W -f='${Status}' $REQUIRED_PKG 2>/dev/null | grep -c "ok installed")
if [ $PKG_OK -eq 0 ];
then
	apt-get -y update
	apt-get -y install nginx
	ufw allow 'Nginx HTTP'
fi

mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
  </html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data
sed -i '/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/;}' /etc/nginx/sites-available/default
service nginx restart
exit 0
