Sol.1

`sudo vi ~/.ssh/config`

```
Host 124.156.119.138
    ProxyCommand          nc -X connect -x proxy_host:proxy_port %h %p
    ServerAliveInterval   10
```



Sol.2

```
ssh USER@FINAL_DEST -o "ProxyCommand=nc -X connect -x PROXYHOST:PROXYPORT %h %p"
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbOTIwOTU4NTM2XX0=
-->