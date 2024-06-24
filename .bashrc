PS1='[\033[32m\w\033[0m]\n~> '
bind '"\e[A":history-search-backward'
bind '"\e[B":history-search-forward'

# alias
alias grep='grep -i --color'
alias cp='cp -v'
alias mv='mv -v'
alias rm='rm -v'
alias mkdir='mkdir -p'
alias wget='wget --hsts-file="/wget-hsts"'
alias vim='nvim'
alias ll='eza -lah --color --hyperlink'
alias l='eza -lh --color --hyperlink'
alias serve='python3 -m http.server'
alias o='xdg-open'