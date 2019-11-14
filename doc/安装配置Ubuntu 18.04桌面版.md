# 安装配置Ubuntu 18.04桌面版

## 目标

- Windows系统基础上，再安装Ubuntu 18.04（双系统）
- 完成Ubuntu 18.04的基础配置

## 准备

硬件：
- 一个2GB以上的U盘
- 一台运行Windows系统的电脑

软件：
- Ubuntu 18.04 server ISO 文件，[官网下载](https://ubuntu.com/download/server)
- rufus启动U盘制作工具，[官网下载](https://rufus.ie/)

## 安装Ubuntu 18.04 server

1. 制作启动U盘
2. 切出空闲硬盘
3. BIOS修改启动顺序
4. 重启电脑开始安装
5. 安装Ubuntu Desktop
	```
	sudo apt update && sudo apt upgrade
	sudo apt install tasksel
	sudo tasksel
	```
	使用空格选择Ubuntu Desktop，选中OK回车
6. 修复可能缺失的驱动
	某些电脑不修复显卡驱动，进不去桌面系统
	```
	sudo apt update && sudo apt upgrade
	sudo ubuntu-drivers autoinstall
	```
现在可以reboot重启进入桌面系统了。

## 系统配置

1. 设置静态IP
	```
	sudo vi /etc/netplan/01-netcfg.yaml
	```
	
	修复为：
		```
		network:
		  version: 2
		  renderer: networkd
		  ethernets:
		    enp4s0:
		    ^^^^^^
		      dhcp4: no
		      addresses:
		        - 10.161.32.160/22
		      gateway4: 10.161.32.1
		      nameservers:
		          addresses:
		              [8.8.8.8]
		```

   注意：`enp4s0`是本机的网卡名称，可能会不一样
   使固定IP生效 
	```
	sudo netplan appl
	```
	
<!--stackedit_data:
eyJoaXN0b3J5IjpbNTQ5MTQyMzY0LDQ0MjM5NzY0M119
-->