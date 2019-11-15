# 云服务器创建swap

[https://cloud.tencent.com/document/product/362/3597](https://cloud.tencent.com/document/product/362/3597)

	1. dd if=/dev/zero of=/mnt/swap2g bs=1M count=2048
	2. mkswap /mnt/swap2g
	3. swapon /mnt/swap2g
	4. 修改/etc/fstab文件，在文件最后添加 /mnt/swap2g swap swap defaults 0 0

<!--stackedit_data:
eyJoaXN0b3J5IjpbNjA3MDQ4MTE5XX0=
-->