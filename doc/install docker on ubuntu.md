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

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTc0NzM5ODM4NSw3MzA5OTgxMTZdfQ==
-->