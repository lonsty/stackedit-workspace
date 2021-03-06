# 云服务器创建swap
Reference: [https://cloud.tencent.com/document/product/362/3597](https://cloud.tencent.com/document/product/362/3597)

-   查看系统当前的分区情况`free -m`
-   创建用于交换分区的文件`dd if=/dev/zero of=/xxx/swap bs=4096 count=1572864`
-   设置交换分区文件`mkswap /xxx/swap`
-   启用交换分区文件`swapon /xxx/swap`
-   若要想使开机时自启用，则需修改文件`/etc/fstab`中的swap行`echo “LABEL=SWAP-sda /xxx/swap swap swap defaults 0 0” >> /etc/fstab`
-   删除swap`swapoff /xxx/swap ; rm -f /Application/swap`

**创建swap**

创建用于交换分区的文件

    $ dd if=/dev/zero of=/mnt/swap bs=1M count=4096
 
设置交换分区文件

    $ mkswap /mnt/swap

启用交换分区文件

    $ swapon /mnt/swap

若要想使开机时自启用，则需在`/etc/fstab`中添加

    /mnt/swap swap swap defaults 0 0

**删除swap**

在`/etc/fstab`中删除

    /mnt/swap swap swap defaults 0 0

关闭并删除分区

    swapoff /mnt/swap
    rm -f /mnt/swap

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTkzODkwMTU0Nl19
-->