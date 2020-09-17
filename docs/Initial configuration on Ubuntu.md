# Initial configuration on Ubuntu

- System: Ubuntu 18.04

## 1. Set static IP address

Edit configurations in file `/etc/netplan/*.yaml`：

```yaml
network:
  version: 2
  renderer: networkd
  ethernets:
    eno1:
      addresses: [10.157.231.37/24]
      gateway4: 10.157.231.1
      nameservers:
        addresses: [10.191.131.131, 10.191.130.130]
```

## 2. Set NTP server

1. Edit configurations in file `/etc/systemd/timesyncd.conf`，add line `NTP=<NTP server>` to `[Time]` section：

```
[Time]
NTP=10.191.131.131
```

2. Restart NTP service：

```sh
sudo service systemd-timesyncd restart
```

## 3. Set system timezone

1. Check timezion information：

```sh
timedatectl
```

2. Set timezone to `Asia/Hong_Kong`：

```sh
sudo timedatectl set-timezone Asia/Hong_Kong
```

3. Restart service to activate the change：

```sh
sudo service systemd-timesyncd restart
```

## 4. Set APT proxy for upgrading packages

1. Add following line to `/etc/apt/apt.conf`：

```
Acquired::http::proxy "http://user:password@host:port";
```

2. Or set environment variables by using `export`：

```sh
export http_proxy="http://user:password@host:port" https_proxy="http://user:password@host:port"
```

3. Or add environment variables to `/etc/environment`:

```
http_proxy="http://user:password@host:port"
https_proxy="http://user:password@host:port"
bo_proxy="localhost"
```

Then run `source /etc/environment` to activate them.

Now it's time to upgrade packages：

```sh
sudo apt update && sudo apt upgrade
```

## 5. Install Docker & docker-compose

Uninstall old versions if these are installed:

```sh
sudo apt-get remove docker docker-engine docker.io containerd runc
```

### Install Docker

1. Update the apt package index and install packages to allow apt to use a repository over HTTPS:

  ```sh
  sudo apt-get update

  sudo apt-get install \
      apt-transport-https \
      ca-certificates \
      curl \
      gnupg-agent \
      software-properties-common
  ```

2. Add Docker’s official GPG key:

  ```sh
  curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -
  ```

  Verify that you now have the key with the fingerprint 9DC8 5822 9FC7 DD38 854A E2D8 8D81 803C 0EBF CD88, by searching for the last 8 characters of the fingerprint.

  ```sh
  sudo apt-key fingerprint 0EBFCD88

  pub   4096R/0EBFCD88 2017-02-22
        Key fingerprint = 9DC8 5822 9FC7 DD38 854A  E2D8 8D81 803C 0EBF CD88
  uid                  Docker Release (CE deb) <docker@docker.com>
  sub   4096R/F273FCD8 2017-02-22
  ```

3. Set up the stable repository:

  ```sh
  sudo add-apt-repository \
     "deb [arch=amd64] https://download.docker.com/linux/debian \
     $(lsb_release -cs) \
     stable"
  ```

4. Install Docker Engine

  ```sh
  sudo apt-get update
  sudo apt-get install docker-ce docker-ce-cli containerd.io
  ```

### Manage Docker as a non-root user

1. Add your user to the docker group.

```sh
sudo usermod -aG docker $USER
```

2. Log out and log back in so that your group membership is re-evaluated.

On Linux, you can also run the following command to activate the changes to groups:

```sh
newgrp docker 
```

3. Verify that you can run docker commands without sudo.

```sh
docker ps
```

### Configure Docker to start on boot

```sh
sudo systemctl enable docker
```

### Set HTTP/HTTPS proxy

1. Create a systemd drop-in directory for the docker service:

```sh
sudo mkdir -p /etc/systemd/system/docker.service.d
```

2. Create a file named `/etc/systemd/system/docker.service.d/http-proxy.conf` that adds the HTTP_PROXY environment variable:

```
[Service]
Environment="HTTP_PROXY=http://proxy.example.com:8080"
```

3. Flush changes and restart Docker

```sh
sudo systemctl daemon-reload
sudo systemctl restart docker
```

4. Verify that the configuration has been loaded and matches the changes you made, for example:

```sh
$ sudo systemctl show --property=Environment docker

Environment=HTTP_PROXY=http://proxy.example.com:80 HTTPS_PROXY=https://proxy.example.com:443 NO_PROXY=localhost,127.0.0.1,docker-registry.example.com,.corp
```

### Custom runtime directory and storage driver

You may want to control the disk space used for Docker images, containers, and volumes by moving it to a separate partition.

1. To accomplish this, set the following flags in the `/etc/docker/daemon.json` file:

```
{
    "data-root": "/mnt/docker-data",
    "storage-driver": "overlay2"
}
```

2. Flush changes and restart Docker

```sh
sudo systemctl daemon-reload
sudo systemctl restart docker
```

### Configuring remote access with daemon.json

1. Set the hosts array in the /etc/docker/daemon.json to connect to the UNIX socket and an IP address, as follows:

```json
{
"hosts": ["unix:///var/run/docker.sock", "tcp://127.0.0.1:2375"]
}
```

2. Restart Docker.

```sh
sudo systemctl restart docker.service
```

3. Check to see whether the change was honored by reviewing the output of netstat to confirm dockerd is listening on the configured port.

```sh
sudo netstat -lntp | grep dockerd
tcp        0      0 127.0.0.1:2375          0.0.0.0:*               LISTEN      3758/dockerd
```

### Install docker-compose

1. Run this command to download the current stable release of Docker Compose:

```sh
sudo curl -L "https://github.com/docker/compose/releases/download/1.27.3/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```

> To install a different version of Compose, substitute 1.27.3 with the version of Compose you want to use.

You may have problems installing with `sudo curl` via proxy, one solution is to switch to root by `sudo su`, then run `curl` without `sudo`.

2. Apply executable permissions to the binary:

```sh
sudo chmod +x /usr/local/bin/docker-compose
```
