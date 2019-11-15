# 云服务器创建swap

[https://cloud.tencent.com/document/product/362/3597](https://cloud.tencent.com/document/product/362/3597)

-   查看系统当前的分区情况`free -m`
-   创建用于交换分区的文件`dd if=/dev/zero of=/xxx/swap bs=4096 count=1572864`
-   设置交换分区文件`mkswap /xxx/swap`
-   启用交换分区文件`swapon /xxx/swap`
-   若要想使开机时自启用，则需修改文件`/etc/fstab`中的swap行`echo “LABEL=SWAP-sda /xxx/swap swap swap defaults 0 0” >> /etc/fstab`
-   删除swap`swapoff /xxx/swap ; rm -f /Application/swap`

创建用于交换分区的文件

    dd if=/dev/zero of=/mnt/swap2g bs=1M count=2048

d
设置交换分区文件

		mkswap /mnt/swap2g

启用交换分区文件

		swapon /mnt/swap2g


		修改/etc/fstab文件，在文件最后添加 /mnt/swap2g swap swap defaults 0 0

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE5ODQ3NTI5NThdfQ==
-->