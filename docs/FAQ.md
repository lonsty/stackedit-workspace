
- [Pip error after update](#pip-error-after-update)

### Pip error after update
> Traceback (most recent call last):  
  &nbsp;&nbsp;&nbsp;&nbsp;File "/usr/bin/pip3", line 9, in <module>  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;from pip import main  
ImportError: cannot import name 'main'

Sol.1:

	hash -d pip3

Sol.2:

	sudo python3 -m pip uninstall pip && sudo apt install python3-pip --reinstall

------------------------------------
### vi 中 `CTRL + S` 卡死？

习惯了使用 `Ctrl + S` 来保存编辑。在 vi 中有时候还会习惯的按 `Ctrl + S`，按完就惊呆了，终端疑似卡死，没反应了。

问题在于 `Ctrl + S` 在 vi 下作用为锁定屏幕，解锁按 `Ctrl + Q` 就可以了。知道真相的我眼泪掉下来!

### MySQL depends on Ubuntu

> flask-sqlacodegen --flask "mysql://root:whsp2020@10.202.16.239:3306/whsp_dev?charset=utf8"

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEwNTE5OTc2OTIsMTY2NzE0MTMxNF19
-->