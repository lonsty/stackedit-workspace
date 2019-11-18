### Pip error after update
> Traceback (most recent call last):
  File "/usr/bin/pip3", line 9, in <module>
    from pip import main
ImportError: cannot import name 'main'

sol.1:

	hash -d pip3
	
sol2:

	sudo python3 -m pip uninstall pip && sudo apt install python3-pip --reinstall
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTY2NzE0MTMxNF19
-->