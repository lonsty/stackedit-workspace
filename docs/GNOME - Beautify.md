# GNOME Preferences

tweak tool
```
sudo apt install gnome-tweaks
```

## GNOME shell extensions

https://extensions.gnome.org/

For Firefox
1. Install GNOME shell extensions
2. Go to https://extensions.gnome.org/ and will see,
> Although GNOME Shell integration extension is running, native host connector is not detected. Refer [documentation](https://wiki.gnome.org/Projects/GnomeShellIntegrationForChrome/Installation) for instructions about installing connector.

For Chrome
https://askubuntu.com/questions/1107848/although-gnome-shell-integration-extension-is-running-native-host-connector-is
```
sudo apt-get install chrome-gnome-shell 
```
```
sudo apt-get install gir1.2-gtop-2.0 gir1.2-networkmanager-1.0  gir1.2-clutter-1.0
```
`Alt` + `F2`, type `r` then `Enter`.

extensions:
- User Themes
- Dash to dock
- 

## Icons

Extract to `/usr/share/icons` or `$HOME/.icons` or `$HOME/.local/share/icons`

- Papirus
[https://github.com/PapirusDevelopmentTeam/papirus-icon-theme](https://github.com/PapirusDevelopmentTeam/papirus-icon-theme)
	```
	sudo add-apt-repository ppa:papirus/papirus
	sudo apt-get update
	sudo apt-get install papirus-icon-theme
	```

- Tela-icon-theme
[https://github.com/vinceliuice/Tela-icon-theme](https://github.com/vinceliuice/Tela-icon-theme)

    `./install.sh`  [OPTIONS]  [COLOR VARIANTS]

## Themes

## Grub themes

## Shell themes

## Profiles
> [How to export a gnome-terminal profile?](https://unix.stackexchange.com/questions/448811/how-to-export-a-gnome-terminal-profile)
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTA5MjM2MTE5OCwtMTYzNTkyOTkxMF19
-->