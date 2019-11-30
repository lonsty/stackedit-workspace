> vi将tab键替换为4个空格
[https://www.jianshu.com/p/52fbe68cf6b6](https://www.jianshu.com/p/52fbe68cf6b6)

### 1. 编辑文件：

```undefined
vi /etc/vim/vimrc
```

### 2. 配置缩进：

```bash
set tabstop=4       " Tab键替换的空格长度，默认8
set softtabstop=4   " 退格键退回缩进空格的长度
set shiftwidth=4    " 表示每一级缩进的长度
set expandtab       " 设置缩进用空格来表示
```

### 3. 配置自动缩进（可选）：

写代码时，按换行键，如果需要让代码自动缩进一个Tab，可以增加以下配置

```bash
set autoindent      " 设置自动缩进
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIwNTQyMDEwNjRdfQ==
-->