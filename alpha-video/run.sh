#!/bin/sh
CONFIG_PATH=/data/options.json
subdomain="$(jq --raw-output 'subdomain' $CONFIG_PATH)" 
export subdomain

echo "For support please visit the Github Project or send a message on our Discord server."
echo "set nameserver to 1.1.1.1"
echo nameserver 1.1.1.1 > /etc/resolv.conf
echo "Starting Alpha-Video"
python3 /app/main.py > /var/log/alpha-video.log&
echo "Starting Supervisord"
/usr/bin/supervisord -n -c /etc/supervisor/supervisord.conf
bash
