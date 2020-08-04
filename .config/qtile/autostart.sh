#!/bin/sh

# Reverse Scrolling
xinput --set-prop 13 326 -108, -108

# Faster Cursor
xset r rate 250 45

# Disable trackpad while typing
syndaemon -K -i 0.5 -R -d 

# Audio
pulseaudio --start

# Wallpaper
feh --bg-fill ~/.config/wallpaper/sky.jpg
