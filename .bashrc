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

PS1='\W \$ '

BASE16_SHELL="$HOME/.config/base16-shell/"
[ -n "$PS1" ] && \
    [ -s "$BASE16_SHELL/profile_helper.sh" ] && \
    eval "$("$BASE16_SHELL/profile_helper.sh")"
