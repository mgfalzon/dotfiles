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
alias magit='vim -c MagitOnly'
alias s='vim -c :Files'
alias config='cd ~/.config'
alias picom='picom --experimental-backends --backend glx'
alias task='clear && task'
alias t='task'
alias tl='task list'
alias audio='alsamixer'

export PATH="$HOME/.config/bin:$PATH"
export PATH="$HOME/.local/bin:$PATH"
export PATH="$HOME/.opam/default/bin:$PATH"
export PATH="$(ruby -e 'puts Gem.user_dir')/bin:$PATH"
export FZF_DEFAULT_COMMAND='rg --files --sort-files'
# --hidden on fzf

PS1='\W \$ '

# BASE16_SHELL
BASE16_SHELL="$HOME/.config/base16-shell/"
[ -n "$PS1" ] && \
    [ -s "$BASE16_SHELL/profile_helper.sh" ] && \
    eval "$("$BASE16_SHELL/profile_helper.sh")"
