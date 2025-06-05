if status is-interactive
    # To reload fish configuration
    # source ~/.config/fish/config.fish
    alias reload="source ~/.config/fish/config.fish"
    alias nfish="nvim ~/.config/fish/config.fish"

    # Commands to run in interactive sessions can go here
    fastfetch

    # aliases
    alias cdwm="nvim ~/Builds/dwm-btw/config.h"
    alias e="nvim"
    alias mdwm="cd ~/Builds/dwm-btw/; sudo make clean install; cd -"
    alias ehypr="nvim ~/.config/hypr/hyprland.conf"
    alias wiki="nvim ~/vimwiki/index.md"
    alias ewiki="nvim ~/.config/nvim/lua/plugins/vimwiki.lua"

    # set default editor
    set -Ux EDITOR nvim
    set -Ux VISUAL nvim
end
