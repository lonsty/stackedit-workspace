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
	sudo netplan apply
	```
	验证是否修改成功
	```
	ip addr show enp4s0
	```

2. 修复双系统时区不一致问题
	```
	timedatectl set-local-rtc 1 --adjust-system-clock
	```
3. 安装中文输入法
4. 关闭系统程序问题检测
	[https://itsfoss.com/how-to-fix-system-program-problem-detected-ubuntu/](https://itsfoss.com/how-to-fix-system-program-problem-detected-ubuntu/)
![Ubuntu has experienced an internal error](https://i2.wp.com/itsfoss.com/wp-content/uploads/2015/07/Ubuntu_Internal_error.png?ssl=1)
	```
	sudo rm /var/crash/*
	```
	```
	sudo vi /etc/default/apport
	```
	修改`enabled=1`为`enabled=0`
5. 修复开关机长时间等待问题
	- [A start job is running for wait for network to be configured. Ubuntu server](https://askubuntu.com/questions/972215/a-start-job-is-running-for-wait-for-network-to-be-configured-ubuntu-server-17-1)
		Use
		```
		systemctl disable systemd-networkd-wait-online.service
		```
		to disable the wait-online service to prevent the system from waiting on a network connection, and use
		```
		systemctl mask systemd-networkd-wait-online.service
		```
		to prevent the service from starting if requested by another service (the service is symlinked to  `/dev/null`).
	- 开机长时间等待设定
		```
		sudo vim /etc/systemd/system/network-online.target.wants/networking.service
		```
				    
		TimeoutStartSec=5min --> TimeoutStartSec=1sec
	- 关机长时间等待设定  
		```
		sudo vim /etc/systemd/system.conf
		```
		DefaultTimeoutStartSec=9s
		DefaultTimeoutStopSec=9s
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTY2NzIyOTkyMl19
-->