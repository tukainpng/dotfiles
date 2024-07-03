#
# ~/.bash_profile
#

export PATH="$HOME/.local/bin:$PATH"
export EDITOR="nvim"
[ "$(tty)" == "/dev/tty1" ] && dbus-run-session sway
#[ "$(tty)" == "/dev/tty1" ] && dbus-run-session startxfce4

[[ -f ~/.bashrc ]] && . ~/.bashrc
