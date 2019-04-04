

docker基本命令
---------------------------
- 卸载旧版本docker
	```bash
	sudo apt-get remove docker-ce docker-engine docker.io
	```
- 安装传输环境
	```bash
	sudo apt-get update
	sudo apt-get install apt-transport-https ca-certificates curl software-properties-common
	```
#### 通过apt安装
- 安装软件源GPG 密钥
	```bash
	curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
	# 国内源
	curl -fsSL https://mirrors.ustc.edu.cn/docker-ce/linux/ubuntu/gpg | sudo apt-key add -
	```
- 向 source.list 中添加 Docker 软件源
	```bash
	sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
	# 国内源
	sudo add-apt-repository "deb [arch=amd64] https://mirrors.ustc.edu.cn/docker-ce/linux/ubuntu $(lsb_release -cs) stable"
	```
- 安装
	```bash
	sudo apt-get update
	sudo apt-get install docker-ce[=18.06.1~ce~3-0~ubuntu]
	```
#### 使用脚本自动安装

```bash
curl -fsSL get.docker.com -o get-docker.sh
sudo sh get-docker.sh [--mirror Aliyun]
```
- 启动docker
	```bash
	sudo systemctl enable docker
	sudo systemctl start docker
	```
- 添加用户组
	```bash
	sudo groupadd docker
	sudo usermod -aG docker $USER
	```
- 添加至root用户组
	```bash
	sudo gpasswd -a ${USER} docker
	sudo service docker restart
	newgrp - docker
	```
    - 重启Terminal
   
- 设置代理
	```bash
	sudo mkdir /etc/systemd/system/docker.service.d
	sudo vi /etc/systemd/system/docker.service.d/http-proxy.conf 
	```
	添加以下内容
	```
	[Service]
	Environment="HTTP_PROXY=http://proxy.example.com:80/" "HTTPS_PROXY=http://proxy.example.com:80/"
	```
	重载配置，重启docker
	```bash
	sudo systemctl daemon-reload
	sudo systemctl restart docker
	 ```
- 测试是否安装成功
	```bash
	docker run hello-world
	```
- 清理容器
    - 删除tag为<None>的镜像 
	```bash
	docker rmi $(docker images | grep "<none>")
	```
    - 删除已停止的容器
	```bash
	docker rm $(docker ps -a -q)
	```
- 根据dockerfile搭建镜像，Dockerfile所在文件夹下
	```bash
	docker build -t f1 .
	```
- 导出镜像
	```bash
    docker save -o <package name> <image id/tag>
    docker save <image id/tag> > <package name> 
	```
- 导入镜像
	```bash
    docker load --input  <package name>
    docker load < <package name> 
	```
- 导出容器
	```bash
	docker export  <container id/tag> > <package name> 
	```
- 导入容器
	```bash
    docker import <package name>
    # 方法2 
    cat <package name> | docker import - <repository name>
	```
- 为镜像添加标签
	```bash
    docker tag <image id> <tag nmame>
	```
    - 当tag一开始为none时则打上新标签，否则创建新镜像
- 映射端口
	```bash
	# （本机端口：docker内部端口）
    docker run -p 8080:8080
	```
- 映射数据
    - 映射数据卷Volume(推荐)
        -docker创建管理，易备份迁移，不随docker container销毁而销毁，可被不同container挂载，可设置读写权限 
    - 映射主机文件夹(不推荐)
        - 主机创建，主机文件夹可被docker container修改，不安全，适用于配置文件映射
        - `docker run -v $(pwd)/config:/app/config`（本机文件夹绝对路径：docker文件夹）
    - 映射内存
        - 数据不持久化
        - 高性能
- 进入容器bash界面
	```bash
	docker exec -it <container id> /bin/bash
	```
- commit提交修改
	```bash
	docker commit [选项] <容器ID或容器名> [<仓库名>[:<标签>]]
	```
    - 不推荐使用commit生成镜像，因为黑箱操作，不能还原过程。应使用Dockerfile生层镜像

- 推送到远端仓库
```bash
docker login
docker tag <image> <dockerhub id
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIxNjcwMTA0LDE4NjQxMTc0NDNdfQ==
-->