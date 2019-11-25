# Start MySQL Server with Dokcer

### Step 1: Get the docker image of MySQL

```
docker pull mysql:5.7.28
```

### Step 2: Start running a docker container from MySQL image

```
docker run -d -p 3306:3306 --name mysql mysql:5.7.28
```


### Step 3: Connecting to the MySQL Server instance

```
# Connect to MySQL
docker exec -it mysql mysql -uroot -p

# Create user
CREATE USER 'username'@'host' IDENTIFIED BY 'password';

# Grant privileges
GRANT ALL privileges ON databasename.tablename TO 'username'@'host' WITH GRANT OPTION;
```

- `host` may be `localhost` or `xxx.xxx.xxx.xxx` or `%`
- `*.*` means all databases and all tables
<!--stackedit_data:
eyJoaXN0b3J5IjpbOTg3OTA0MTc5XX0=
-->