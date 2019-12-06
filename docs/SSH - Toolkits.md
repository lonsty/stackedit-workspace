### Using proxy

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


### [Automatically add a new host to known_hosts](https://serverfault.com/questions/132970/can-i-automatically-add-a-new-host-to-known-hosts)
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTY2NDU4NjU1M119
-->