export ZSH="$HOME/.oh-my-zsh"
plugins=(git)
source $ZSH/oh-my-zsh.sh
#
qr() { qrencode -s 15 -o - "$@" | feh - }
function acp() {
  git add .
  git commit -m "$1"
  git push origin $(git symbolic-ref --short HEAD)
}
#
alias update="yay -Syu && flatpak update -y && bun update -g && flatpak remove --unused -y && yay -Yc"
alias c="code-insiders"
alias ls="eza --icons --group-directories-first"
alias lt="ls -T"
alias cmatrix="cmatrix -C cyan"
alias clear="printf '\033[2J\033[3J\033[1;1H'"
alias _nmap='sudo nmap -T5 -n'
alias sc="python ~/Dropbox/Sync/sync.py"
#
eval "$(starship init zsh)"
fpath+=~/.zfunc; autoload -Uz compinit; compinit
#
[ -s "/home/r/.bun/_bun" ] && source "/home/r/.bun/_bun"
#
[ "$(< /proc/$PPID/comm)-${PWD}" = "kitty-${HOME}" ] && fastfetch
[ "$(< /proc/$PPID/comm)-${PWD}" = "alacritty-${HOME}" ] && fastfetch
