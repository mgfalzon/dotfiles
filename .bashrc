#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
# PS1='[\u@\h \W]\$ '

# Matt's Config
alias fgsm='cd /opt/lampp/htdocs/FGSM'
alias xampp='sudo /opt/lampp/xampp'
alias vifm='vifm .'
alias config='cd ~/.config'
alias magit='vim -c MagitOnly'

PS1='\W \$ '

# rofi
#alias rofi='rofi -sidebar-mode \
#-modi run,drun,window \
#-lines 12 \
#-padding 18 \
#-width 60 \
#-location 0 \
#-show drun \
#-columns 3 \
#-font "Ubuntu Mono 12" \'

# picom
alias picom='picom --experimental-backends --backend glx'

# BASE16_SHELL
BASE16_SHELL="$HOME/.config/base16-shell/"
[ -n "$PS1" ] && \
    [ -s "$BASE16_SHELL/profile_helper.sh" ] && \
    eval "$("$BASE16_SHELL/profile_helper.sh")"
