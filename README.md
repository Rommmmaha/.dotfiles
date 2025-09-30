# Arch Linux Dotfiles

This repository contains my personal dotfiles configuration for Arch Linux, optimized for the Hyprland Wayland compositor. It provides a minimal, efficient, and customizable setup for daily use, focusing on productivity and clean color-independent aesthetics.

## Features

- **Window Manager**: [Hyprland](https://hypr.land) with custom keybinds (Super key as main modifier), dwindle layout, no gaps/borders, and animations disabled for performance. Includes Hyprlock for screen locking and Hyprpaper for wallpapers.
- **Shell**: [Zsh](https://sourceforge.net/p/zsh/code/ci/master/tree/) with [Oh My Zsh](https://github.com/ohmyzsh/ohmyzsh/), plugins (z, git, archlinux, [zsh-autosuggestions](https://github.com/zsh-users/zsh-autosuggestions), [fast-syntax-highlighting](https://github.com/zdharma-continuum/fast-syntax-highlighting)), [Starship](https://github.com/starship/starship) prompt, and aliases (e.g., `ls` -> [eza](https://github.com/eza-community/eza), `update` for system updates via [yay](https://github.com/Jguer/yay)/[flatpak](https://github.com/flatpak/flatpak)/[bun](https://github.com/oven-sh/bun)).
- **Terminal**: [Kitty](https://github.com/kovidgoyal/kitty) with [JetBrains Mono Nerd Font](https://github.com/ryanoasis/nerd-fonts), semi-transparent background, and custom cursor.
- **Launcher**: [Rofi](https://github.com/davatorium/rofi) ([Spotlight theme](https://github.com/newmanls/rofi-themes-collection/blob/master/themes/spotlight-dark.rasi)) for apps, run dialog, [emoji picker](https://github.com/fdw/rofimoji), and clipboard history via [Cliphist](https://github.com/sentriz/cliphist).
- **Notifications**: [Mako](https://github.com/emersion/mako) with semi-transparent black background.
- **File Manager**: [Dolphin](https://github.com/KDE/dolphin) with compact mode and custom settings.
- **Editor**: [Micro](https://github.com/zyedidia/micro) with simple colorscheme and comment bindings.
- **Media Player**: [MPV](https://github.com/mpv-player/mpv) with keep-open and position saving.
- **Screenshot Tool**: [Flameshot](https://github.com/flameshot-org/flameshot) with GUI capture and fixed save path.
- **System Monitor**: [Btop](https://github.com/aristocratos/btop) with Adapta theme, Braille graphs, and process sorting.
- **Audio**: [Pipewire](https://github.com/PipeWire/pipewire) with custom configs for larger buffers, mic loopback, virtual sinks (First/Second Dummy), and volume control scripts.
- **Themes**: Breeze-Dark for [GTK3/4](https://invent.kde.org/plasma/breeze-gtk) and [QT6](https://github.com/KDE/breeze) (via [qt6ct-kde](https://www.opencode.net/trialuser/qt6ct)), [GoogleDot-Black cursor](https://github.com/ful1e5/Google_Cursor), Adwaita Sans font.

Custom scripts in `.config/hypr/custom/` handle autostart window placement, PTT overlay (via way-overlay/ncat), output switching, and volume control.

## Installation

1. Clone this repo to `~/.dotfiles` (or your preferred location).
2. You may want to add next lines to `~/.stow-global-ignore`:

  ```text
  hypr/custom/
  mimeapps\.list
  pipewire/
  ```

3. Use [GNU Stow](https://www.gnu.org/software/stow/) for symlinking: `cd ~/.dotfiles ; stow .`.
4. Install dependencies (see below).

**Note**: Some configs assume specific hardware (e.g., NVIDIA GPU in Pipewire/Hyprland). Adjust monitors/devices in `hyprland-device.conf`.

## Dependencies

### Core Packages (pacman)

- `zsh` (shell)
- `hyprland` (WM)
- `hyprlock` (lock screen)
- `hyprpaper` (wallpaper daemon)
- `kitty` (terminal)
- `rofi` (launcher)
- `mako` (notifications)
- `flameshot` (screenshots)
- `btop` (system monitor)
- `cliphist` (clipboard manager)
- `fsearch` (file search)
- `dolphin` (file manager)
- `mpv` (media player)
- `micro` (editor)
- `pipewire` `wireplumber` (audio)
- `qt6ct` (QT config)
- `breeze` `breeze-gtk` (theme/icons)
- `eza` (modern ls)
- `starship` (prompt)
- `fastfetch` (system info)
- `cmatrix` (matrix screensaver)
- `yay` (AUR helper)
- `flatpak` (app store)
- `bun` (JS runtime)
- `ark` (archive tool)
- `qview` (image viewer)
- `kdeconnect` (device sync)
- `xdg-desktop-portal-hyprland` (portals)
- `polkit` `hyprpolkitagent` (auth)
- `wl-clipboard` (Wayland clipboard)
- `python` `jq` `nmap` (scripting)
- `gtk3` `gtk4` (GTK)
- `font-adwaita` (fonts)

### AUR Packages (via yay)

- `zsh-autosuggestions`
- `zsh-syntax-highlighting` (fast-syntax-highlighting)
- `oh-my-zsh-git`
- `wl-clip-persist` (clipboard persistence)
- `way-overlay` (custom built overlay for PTT)
- `scrcpy` (Android audio mirroring, via Python script)
- `rofimoji` (emoji picker)

### Flatpaks (optional, from aliases)

- `com.saivert.pwvucontrol`
