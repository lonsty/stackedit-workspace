#Ubuntu 18.04安装搜狗拼音中文输入法

参考：https://www.jianshu.com/p/c936a8a2180e

卸载ibus。
```shell
sudo apt purge ibus
```

卸载顶部面板任务栏上的键盘指示。
```shell
sudo  apt remove indicator-keyboard
```

安装fcitx输入法框架
```shell
sudo apt install fcitx-table-wbpy fcitx-config-gtk
```

切换为 Fcitx输入法
```shell
im-config -n fcitx
```

im-config 配置需要重启系统才能生效
```shell
sudo shutdown -r now
```

[下载搜狗输入法](http://cdn2.ime.sogou.com/dl/index/1571302197/sogoupinyin_2.3.1.0112_amd64.deb?st=xGC2le_IHhwhsXrb64ahHQ&e=1573724074&fn=sogoupinyin_2.3.1.0112_amd64.deb)
```shell
wget http://cdn2.ime.sogou.com/dl/index/1571302197/sogoupinyin_2.3.1.0112_amd64.deb?st=xGC2le_IHhwhsXrb64ahHQ&e=1573724074&fn=sogoupinyin_2.3.1.0112_amd64.deb
```

安装搜狗输入法
```shell
sudo dpkg -i sogoupinyin*.deb
```

修复损坏缺少的包
```shell
 sudo apt install -f
```

打开 Fcitx 输入法配置
```shell
fcitx-config-gtk3
```

问题: 输入法皮肤透明
```
fcitx设置 >> 附加组件 >> 勾选高级 >> 取消经典界面

Configure >>  Addon >> Advanced >> Classic
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbODEwNTExODgyXX0=
-->