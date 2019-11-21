Sol.1
```
sudo vi ~/.ssh/config


```



Sol.2
```
ssh USER@FINAL_DEST -o "ProxyCommand=nc -X connect -x PROXYHOST:PROXYPORT %h %p"
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE3OTE2MDc0MzldfQ==
-->