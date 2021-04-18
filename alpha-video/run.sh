#!/bin/sh
echo "          _      _____  _    _           __      _______ _____  ______ ____  "
echo "    /\   | |    |  __ \| |  | |   /\     \ \    / /_   _|  __ \|  ____/ __ \ "
echo "   /  \  | |    | |__) | |__| |  /  \     \ \  / /  | | | |  | | |__ | |  | |"
echo "  / /\ \ | |    |  ___/|  __  | / /\ \     \ \/ /   | | | |  | |  __|| |  | |"
echo " / ____ \| |____| |    | |  | |/ ____ \     \  /   _| |_| |__| | |___| |__| |"
echo "/_/    \_\______|_|    |_|  |_/_/    \_\     \/   |_____|_____/|______\____/ "

echo "For support please visit the Github Project or send a message on our Discord server."
echo "set nameserver to 1.1.1.1"
echo nameserver 1.1.1.1 > /etc/resolv.conf
echo "Starting Alpha-Video"
python /app/main.py > /var/log/alpha-video.log&
echo "Starting Supervisord"
/usr/bin/supervisord -n -c /etc/supervisor/supervisord.conf
bash
