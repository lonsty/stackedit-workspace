# SSH 密码自动填充

### 方法一： 使用密钥

在本机生成密钥，并将公钥上传至服务器。

```sh
# 生成密钥
$ ssh-keygen

# 上传至服务器
$ ssh-copy-id <USER>@<HOST> [-p <PORT>]
```
之后就可以直接通过 `ssh <USER>@<HOST> [-p <PORT>]` 登录服务器。

#### 优点

- 不出现明文密码，（妥善保管私钥下）非常安全。

#### 缺点 

- 某些服务器会通过设置，禁用客户端通过公钥登录，使得此方法不适用。

### 方法二： 重写 SSH

> :warning: 此方法依赖于密码填充工具 `sshpass`。

1.  安装 `sshpass`

```sh
$ sudo apt install sshpass
```

2. 使用脚本重新封装 `ssh` 命令
在 `~/.bashrc` （或 `~/.zshrc`）文件末尾添加如下脚本：

	```sh
	# ssh autofill password
	function ssh(){
	  sshhost=$1
	  password=`awk "/#Password/ && inhost { print \\\$2 } /Host/ { inhost=0 } /Host.*?${sshhost}/ { inhost=1 }" ~/.ssh/config`
	  if [[ -z "${password}" ]]; then
	    /usr/bin/ssh $*
	  else
	    sshpass -p ${password} /usr/bin/ssh $*
	  fi
	}
	```
	
	然后运行 `source ~/.bashrc` 使修改生效。
	
3. 将各服务器的主机与密码写入配置文件

打开文件 `~/.ssh/config` （若文件不存在就创建），按如下格式添加配置：

```
# 服务器 IP 或 域名
Host 10.157.138.120 10.202.16.239 10.202.16.240 10.202.16.241
# 登录用户名
    User apadmin
    #Password Foxconn123
```

- `Host`： 服务器 IP 或 域名，
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTc0Mjc5MzAzOF19
-->