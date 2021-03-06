# intellij IDEA

[https://www.jetbrains.com/idea/download/#section=linux](https://www.jetbrains.com/idea/download/#section=linux)

 ### Linux Installation Instructions
  1. Unpack the IntelliJ IDEA distribution archive that you downloaded to
     where you wish to install the program. We will refer to this destination
     location as your {installation home} below.

  2. Open a console and cd into "{installation home}/bin" and type:

       ./idea.sh

     to start the application. As a side effect, this will initialize various
     configuration files in the ~/.IntelliJIdea2019.1 directory.

  3. [OPTIONAL] Add "{installation home}/bin" to your PATH environment
     variable so that you may start IntelliJ IDEA from any directory.

  4. [OPTIONAL] To adjust the value of the JVM heap size, create
      ~/.IntelliJIdea2019.1/config/idea.vmoptions (or idea64.vmoptions
      if using a 64-bit JDK), and set the -Xms and -Xmx parameters. To see how
      to do this, you can reference the vmoptions file under
      "{installation home}/bin" as a model.

 ### [OPTIONAL] Changing the location of "config" and "system" directories
  By default, IntelliJ IDEA stores all your settings under the ~/.IntelliJIdea2019.1/config
  directory and uses ~/.IntelliJIdea2019.1/system as a data cache.
  If you want to change these settings,

  1. Open a console and cd into ~/.IntelliJIdea2019.1/config

  2. Create the file "idea.properties" and open it in an editor. Set the
     idea.system.path and/or idea.config.path variables as desired, for
     example:

     idea.system.path=~/custom/system
     idea.config.path=~/custom/config

  3. Note that we recommend to store data cache ("system" directory) on a disk
     with at least 1GB of free space.
     
### 激活码
[http://idea.lanyus.com/](http://idea.lanyus.com/)

### 热部署&热加载
[https://www.cnblogs.com/jun1019/p/8074448.html](https://www.cnblogs.com/jun1019/p/8074448.html)

[https://www.cnblogs.com/jiangbei/p/8439394.html](https://www.cnblogs.com/jiangbei/p/8439394.html)

# eclipse

[https://www.eclipse.org/downloads/](https://www.eclipse.org/downloads/)

[https://www.eclipse.org/downloads/packages/](https://www.eclipse.org/downloads/packages/)

### ubuntu代理设置失效问题
`去掉socks代理设置，即可连接网络`

### Install JDK 
#### Oracle JDK(tar.gz intsall)
[https://www.javahelps.com/2015/03/install-oracle-jdk-in-ubuntu.html](https://www.javahelps.com/2015/03/install-oracle-jdk-in-ubuntu.html)

#### Oracle JDK(APT intsall)
```bash
sudo add-apt-repository ppa:webupd8team/java
sudo apt-get update
# Oracle JDK 8
sudo apt-get install oracle-java8-installer
```
- Managing Java
```bash
sudo update-alternatives --config java
```
- Setting the JAVA_HOME Environment Variable
```bash
sudo bash -c "echo -e '\nJAVA_HOME=\"/usr/lib/jvm/java-8-oracle\"' >> /etc/environment"
source /etc/environment
```
### 安装maven
#### 官方安装文档
Detailed steps are:

-   Ensure  JAVA_HOME  environment variable is set and points to your JDK installation
-   Extract distribution archive in any directory
```bash
unzip apache-maven-3.6.0-bin.zip
```
or
```bash
tar xzvf apache-maven-3.6.0-bin.tar.gz
```
Alternatively use your preferred archive extraction tool.

-   Add the  bin  directory of the created directory  apache-maven-3.6.0  to the  PATH  environment variable
	-   Adding to  PATH
	```bash
	export PATH=/opt/apache-maven-3.6.0/bin:$PATH
	```
-   Confirm with  `mvn -v`  in a new shell. The result should look similar to
```
Apache Maven 3.6.0 (97c98ec64a1fdfee7767ce5ffb20918da4f719f3; 2018-10-24T20:41:47+02:00)
Maven home: /opt/apache-maven-3.6.0
Java version: 1.8.0_45, vendor: Oracle Corporation
Java home: /Library/Java/JavaVirtualMachines/jdk1.8.0_45.jdk/Contents/Home/jre
Default locale: en_US, platform encoding: UTF-8
OS name: "mac os x", version: "10.8.5", arch: "x86_64", family: "mac"
```

#### 设置代理
```bash
sudo vim {MAVEN_HOME}/conf/settings.xml
```
```xml
<proxies>
    <!-- proxy
     | Specification for one proxy, to be used in connecting to the network.
     |
    <proxy>
      <id>optional</id>
      <active>true</active>
      <protocol>http</protocol>
      <username>proxyuser</username>
      <password>proxypass</password>
      <host>proxy.host.net</host>
      <port>80</port>
      <nonProxyHosts>local.net|some.host.com</nonProxyHosts>
    </proxy>
    -->
	
	<proxy>
      <id>optional</id>
      <active>true</active>
      <protocol>http</protocol>
      <username>mkyong</username>
      <password>password</password>
      <host>proxy.mkyong.com</host>
      <port>8888</port>
      <nonProxyHosts>local.net|some.host.com</nonProxyHosts>
    </proxy>
	
  </proxies>
```

# visual studio code

[https://code.visualstudio.com/download](https://code.visualstudio.com/download)

```bash
sudo dpkg -i *.deb
```

# jupyter
- 安装pip3
```bash
sudo apt install python3-pip
```
- 升级pip
```bash
sudo pip install --upgrade pip
```
- 修复pip3无法使用问题
```bash
sudo vim /usr/bin/pip3
```
```py
#!/usr/bin/python3
# GENERATED BY DEBIAN

import sys

# Run the main entry point, similarly to how setuptools does it, but because
# we didn't install the actual entry point from setup.py, don't use the
# pkg_resources API.
# from pip import main
from pip import __main__
if __name__ == '__main__':
    # sys.exit(main())
    sys.exit(__main__._main())
```
- 安装jupyter
```bash
sudo -H pip3 install jupyter
```
- 配置jupyter
```
ipython

from notebook,auth import passwd
passwd()
```
```
jupyter notebook --generate-config
```
```bash
vim .jupyter/jupyter_notebook_config.py
```
```py
c.NotebookApp.ip='0.0.0.0'
c.NotebookApp.password = u'sha1:17e055146f93:1450e0a31f8971387b3ca4dd82a19ee1f0c1ec59'
c.NotebookApp.open_browser = False
c.NotebookApp.port =8888
c.NotebookApp.allow_root = True
```

# virtualenv
- 安装
```bash
sudo -H pip3 install virtualenv
```
- 使用
```bash
virtualenv --no-site-packages -p python3 venv
source /venv/bin/activate
# 退出
deactivate
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTQ2MTI3Njc2NF19
-->