#!/bin/sh
picom -b &
#/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
#/usr/lib/polkit-kde-authentication-agent-1 &
setxkbmap -layout gb &
lxsession &
eww open volumeh &
eww open mine &
nitrogen --restore &
eww open albumart &
eww open spotify &
conky -c ~/.config/conky/test.conf &
conky -c ~/.config/conky/sidebar.conf &
conky -c ~/.config/conky/weather.conf &
#wal -i git/archcraft-wallpapers/archcraft-backgrounds/files/ &
