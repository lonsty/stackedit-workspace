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
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTY2ODg5NjM3MSwtNjk0OTc4NTM2XX0=
-->