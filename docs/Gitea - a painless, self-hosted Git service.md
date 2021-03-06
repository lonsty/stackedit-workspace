# Gitea: a painless, self-hosted Git service

## Start with docker-compose

Add following to `docker-compose.yml`.

```yml
version: "2"

networks:
  gitea:
    external: false

volumes:
  gitea:
    driver: local
    driver_opts:
      device: /mnt/data/opt/git-space/gitea
      o: bind
      type: none
  mysql:
    driver: local
    driver_opts:
      device: /mnt/data/opt/git-space/mysql
      o: bind
      type: none

services:
  server:
    image: gitea/gitea:latest
    environment:
      - USER_UID=1000
      - USER_GID=1000
      - DB_TYPE=mysql
      - DB_HOST=db:3306
      - DB_NAME=gitea
      - DB_USER=gitea
      - DB_PASSWD=gitea
    restart: always
    networks:
      - gitea
    volumes:
      - gitea:/data
      - /etc/timezone:/etc/timezone:ro
      - /etc/localtime:/etc/localtime:ro
    ports:
      - "80:3000"
      - "222:22"
    depends_on:
      - db

  db:
    image: mysql:5.7
    restart: always
    environment:
      - MYSQL_ROOT_PASSWORD=gitea
      - MYSQL_USER=gitea
      - MYSQL_PASSWORD=gitea
      - MYSQL_DATABASE=gitea
    networks:
      - gitea
    volumes:
      - mysql:/var/lib/mysql
```

## Start up MySQL and Gitea service

```sh
docker-compose up -d
```

## Configure at first login

Go to http://localhost, and complete the settings.

## Upgrade Gitea

❗❗ Make sure you have volumed data to somewhere outside Docker container.

To upgrade your installation to the latest release:

```
# Edit `docker-compose.yml` to update the version, if you have one specified
# Pull new images
docker-compose pull
# Start a new container, automatically removes old one
docker-compose up -d
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEwNjQxMjI3ODIsLTY5NDk3ODUzNl19
-->