
#### SET UP THE REPOSITORY

1.  Update the  `apt`  package index:
    
    ```
    $ sudo apt-get update
    ```
    
2.  Install packages to allow  `apt`  to use a repository over HTTPS:
    
    ```
    $ sudo apt-get install \
        apt-transport-https \
        ca-certificates \
        curl \
        software-properties-common
    ```
    
3.  Add Docker’s official GPG key:
    
    ```
    $ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    ```

	> curl: (35) error:1408F10B:SSL routines:ssl3_get_record:wrong version number
gpg: no valid OpenPGP data found.

	Sol.
	```
	export https_proxy=http://10.57.197.116:50030
	```
    
    Verify that you now have the key with the fingerprint  `9DC8 5822 9FC7 DD38 854A E2D8 8D81 803C 0EBF CD88`, by searching for the last 8 characters of the fingerprint.
    
    ```
    $ sudo apt-key fingerprint 0EBFCD88
    
    pub   4096R/0EBFCD88 2017-02-22
          Key fingerprint = 9DC8 5822 9FC7 DD38 854A  E2D8 8D81 803C 0EBF CD88
    uid                  Docker Release (CE deb) <docker@docker.com>
    sub   4096R/F273FCD8 2017-02-22
    ```

4. Add apt repository

    ```
    sudo add-apt-repository \
       "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
       $(lsb_release -cs) \
       stable"
    ```

#### INSTALL DOCKER CE

1.  Update the  `apt`  package index.

    ```
    $ sudo apt-get update
    ```
    
2.  Install the latest version of Docker CE, or go to the next step to install a specific version. Any existing installation of Docker is replaced.
    
    ```
    $ sudo apt-get install docker-ce
    ```

3. Start docker on boot

    ```
    $ sudo systemctl enable docker
    ```

4. Work via proxies

	[https://medium.com/@airman604/getting-docker-to-work-with-a-proxy-server-fadec841194e](https://medium.com/@airman604/getting-docker-to-work-with-a-proxy-server-fadec841194e)
		
	```
	mkdir /etc/systemd/system/docker.service.d
	vi /etc/systemd/system/docker.service.d/http-proxy.conf
	```

	```
	[Service]
	Environment="HTTP_PROXY=http://user01:password@10.10.10.10:8080/"
	Environment="HTTPS_PROXY=http://user01:password@10.10.10.10:8080/"
	Environment="NO_PROXY= hostname.example.com,172.10.10.10"
	```

	```
	systemctl daemon-reload
	systemctl restart docker
	```

	Varify
	```
	systemctl show docker --property Environment
	```

#### RUN DOCKER COMMANDS WITHOUT SUDO

1. Add the `docker` group if it doesn't already exist

    ```
    $ sudo groupadd docker
    ```

2. Add the connected user `$USER` to the docker group
    
    Optionally change the username to match your preferred user.

    ```
    $ sudo gpasswd -a $USER docker
    ```

3. Restart the `docker` daemon

    ```
    $ sudo service docker restart
    ```
4. Log out and log in to let it work, or

	```
	newgrp docker
	```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTYwMjYzODU1XX0=
-->