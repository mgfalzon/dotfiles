#!/bin/sh

## Functional ##

# Reverse Scrolling
xinput --set-prop 13 326 -108, -108

# Faster Cursor
xset r rate 250 45

# Disable trackpad while typing
syndaemon -K -i 0.5 -R -d 

# Audio
pulseaudio --start

# Notifications
dunst &

# Low Battery Notification
sh ./battery.sh &


## Visual ##

# Wallpaper
feh --bg-fill ~/.config/wallpaper/dark.png

# Compositor
picom &
