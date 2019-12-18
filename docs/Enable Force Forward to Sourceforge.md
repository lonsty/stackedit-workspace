# Enable Force Forward to Sourceforge

### 1. Login Sourceforge via SSH

If it's your first time to login sourceforge via SSH

```
$ ssh user,passwd@shell.sourceforge.net create
```

else

```
$ ssh user,passwd@shell.sourceforge.net
```

### 2. Change git config

Swhith to the project directory,

```
$ cd /home/git/p/<repository>
```

then edit the config, set `receive.denyNonFastforwards` to `false`

```
$ git config receive.denyNonFastforwards false
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE1OTQ0OTEzOThdfQ==
-->