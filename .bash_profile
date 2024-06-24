#
# ~/.bash_profile
#

export PATH="$HOME/.local/bin:$PATH"
[ "$(tty)" == /dev/tty ] && dbus-run-session sway

[[ -f ~/.bashrc ]] && . ~/.bashrc
