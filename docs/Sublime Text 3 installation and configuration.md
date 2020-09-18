# Sublime Text 3 configuration

## Installation

Install the GPG key:

```sh
wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
```

Ensure apt is set up to work with https sources:

```sh
sudo apt-get install apt-transport-https
```

Select the channel to use:

**Stable**:

```sh
echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list
```

Update apt sources and install Sublime Text

```sh
sudo apt-get update
sudo apt-get install sublime-text
```

## Activation

Sublime text 3 3211

```
----- BEGIN LICENSE -----
Member J2TeaM
Single User License
EA7E-1011316
D7DA350E 1B8B0760 972F8B60 F3E64036
B9B4E234 F356F38F 0AD1E3B7 0E9C5FAD
FA0A2ABE 25F65BD8 D51458E5 3923CE80
87428428 79079A01 AA69F319 A1AF29A4
A684C2DC 0B1583D4 19CBD290 217618CD
5653E0A0 BACE3948 BB2EE45E 422D2C87
DD9AF44B 99C49590 D2DBDEE1 75860FD2
8C8BB2AD B2ECE5A4 EFC08AF2 25A9B864
------ END LICENSE ------
```

## Configurate proxies

`Preferences -> Settings`:

```json
{
    "http_proxy": "",
    "https_proxy": "",
    "proxy_username": "",
    "proxy_password": ""
}
```

## Install package control

Press <kbd>Ctrl</kbd> <kbd>Shift</kbd> <kbd>P</kbd>, then input `IPC` and press <kbd>Enter</kbd>.

## Install packages

Press <kbd>Ctrl</kbd> <kbd>Shift</kbd> <kbd>P</kbd>, then input `PCIP` and press <kbd>Enter</kbd>.

## Packages

- MarkdownEditing
- monokaiC
- MarkdownPreview
- Emmet
- Side​Bar​Enhancements
- BracketHighlighter
- SublimeLinter
  - SublimeLinter-annotations
  - SublimeLinter-contrib-yamllint
  - SublimeLinter-csslint
  - SublimeLinter-eslint
  - SublimeLinter-html-tidy
  - SublimeLinter-jshint
  - SublimeLinter-json
  - SublimeLinter-mdl
  - SublimeLinter-pycodestyle
  - SublimeLinter-rst
  - SublimeLinter-shellcheck
