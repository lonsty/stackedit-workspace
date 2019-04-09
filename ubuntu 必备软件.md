# 搜狗输入法

[http://cdn2.ime.sogou.com/dl/index/1524572264/sogoupinyin_2.2.0.0108_amd64.deb?st=qfXfNN9DE5nr1uivgH3Ynw&e=1554776803&fn=sogoupinyin_2.2.0.0108_amd64.deb](http://cdn2.ime.sogou.com/dl/index/1524572264/sogoupinyin_2.2.0.0108_amd64.deb?st=qfXfNN9DE5nr1uivgH3Ynw&e=1554776803&fn=sogoupinyin_2.2.0.0108_amd64.deb)  
```
sudo dpkg -i install sogou*.deb
sudo apt install -f (解决缺失的依赖)  
sudo dpkg -i install sogou*.deb
```
- logout & login
- config settings add sogou pinyin

# Google chrome
- download google chrome 64 bit *.deb
- install
```
sudo dpkg -i google-chrome*.deb
```
# sublime

- Install the GPG key:
```
wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
```
- Ensure apt is set up to work with https sources:
```
sudo apt-get install apt-transport-https
```
- Stable version:
```
echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list
```
- Update apt sources and install Sublime Text
```
sudo apt-get update
sudo apt-get install sublime-text
```
### 激活码 for 3207
```
ZYNGA INC.
50 User License
EA7E-811825
927BA117 84C9300F 4A0CCBC4 34A56B44
985E4562 59F2B63B CCCFF92F 0E646B83
0FD6487D 1507AE29 9CC4F9F5 0A6F32E3
0343D868 C18E2CD5 27641A71 25475648
309705B3 E468DDC4 1B766A18 7952D28C
E627DDBA 960A2153 69A2D98A C87C0607
45DC6049 8C04EC29 D18DFA40 442C680B

1342224D 44D90641 33A3B9F2 46AADB8F
```

### 修复无法输入中文
- github  [https://github.com/lyfeyaj/sublime-text-imfix](https://github.com/lyfeyaj/sublime-text-imfix)

#### Usage

  

Steps to use this repo:
- Update and then upgrade your system to the newest
```bash
sudo apt-get update && sudo apt-get upgrade
```
- Clone this repo in your local directory :
```bash
git clone https://github.com/lyfeyaj/sublime-text-imfix.git
```
- Change your current directory to `sublime-text-imfix`:
```bash
cd sublime-text-imfix
```
- Run the below script :
```bash
./sublime-imfix
```
- Done! Re-login your X windows. And then you can enjoy using Sublime Text 3 with Fctix Input Method!

#### 安装后问题

命令行`subl`和图标都无法使用，无法打开应用，CPU占用100%
##### 解决方法
1. 修改启动文件，注释掉export行
```bash
sudo vim /usr/bin/subl
```
```bash
#!/bin/sh
# export LD_PRELOAD=/opt/sublime_text/libsublime-imfix.so
exec /opt/sublime_text/sublime_text "$@"
```
2. 修改desktop文件为默认设置
```bash
sudo vim /usr/share/applications/sublime-text.desktop
```
```bash
[Desktop Entry]
Version=1.0
Type=Application
Name=Sublime Text
GenericName=Text Editor
Comment=Sophisticated text editor for code, markup and prose
Exec=/opt/sublime_text/sublime_text %F
#Exec=/usr/bin/subl %F
Terminal=false
MimeType=text/plain;
Icon=sublime-text
Categories=TextEditor;Development;
StartupNotify=true
Actions=Window;Document;
#StartupWMClass=Sublime_text

[Desktop Action Window]
Name=New Window
Exec=/opt/sublime_text/sublime_text -n
#Exec=/usr/bin/subl -n
OnlyShowIn=Unity;
[Desktop Action Document]
Name=New File
Exec=/opt/sublime_text/sublime_text --command new_file
#Exec=/usr/bin/subl --command new_file
OnlyShowIn=Unity;
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTAxODI2MjM3M119
-->