export ZSH="$HOME/.oh-my-zsh"
plugins=(z git archlinux zsh-autosuggestions fast-syntax-highlighting)
source "$ZSH/oh-my-zsh.sh"
[ -s "/home/r/.bun/_bun" ] && source "/home/r/.bun/_bun"

bindkey '^H' backward-kill-word

export EDITOR="micro"

alias update="yay -Syu && flatpak update -y && bun update -g && flatpak remove --unused -y && yay -Yc"
alias c="code-insiders"
alias ls="eza --icons --group-directories-first"
alias tree="ls -T"
alias cmatrix="cmatrix -C cyan"
alias clear="printf '\033[2J\033[3J\033[1;1H'"
alias _nmap='sudo nmap -T5 -n'
alias sc="python ~/Dropbox/Sync/sync.py"
alias edit=$EDITOR

qr() {
  qrencode -s 15 -o - "$@" | feh -
}
acp() {
  git add .
  git commit -m "$1"
  git push origin "$(git symbolic-ref --short HEAD)"
}

eval "$(starship init zsh)"
case "$(< /proc/$PPID/comm)-${PWD}" in "kitty-${HOME}" | "alacritty-${HOME}") fastfetch ;;
esac
