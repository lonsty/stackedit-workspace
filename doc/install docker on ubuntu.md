# Install docker-ce on Ubuntu

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
    
    Verify that you now have the key with the fingerprint  `9DC8 5822 9FC7 DD38 854A E2D8 8D81 803C 0EBF CD88`, by searching for the last 8 characters of the fingerprint.
    
    ```
    $ sudo apt-key fingerprint 0EBFCD88
    
    pub   4096R/0EBFCD88 2017-02-22
          Key fingerprint = 9DC8 5822 9FC7 DD38 854A  E2D8 8D81 803C 0EBF CD88
    uid                  Docker Release (CE deb) <docker@docker.com>
    sub   4096R/F273FCD8 2017-02-22
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

#### Run Docker commands without sudo


##### 1. Add the `docker` group if it doesn't already exist

```console
$ sudo groupadd docker
```

##### 2. Add the connected user `$USER` to the docker group

Optionally change the username to match your preferred user.

```console
$ sudo gpasswd -a $USER docker
```

##### 3. Restart the `docker` daemon

```console
$ sudo service docker restart
```

If you are on Ubuntu 14.04-15.10, use `docker.io` instead:

```console
$ sudo service docker.io restart
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTkyOTU3ODY1Miw3MzA5OTgxMTZdfQ==
-->