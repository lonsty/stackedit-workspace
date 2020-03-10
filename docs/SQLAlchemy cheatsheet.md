## Dadabase Connection

URL format:
- MySQL
```
# requires pip install install mysqlclient
mysql://user:passwd@host:port/database

# requires pip install pymysql
mysql+pymysql://user:passwd@host:port/database
```

- PostgreSQL
```
# requires pip install psycopg2
postgresql://user:passwd@host:port/database
```

## Schema Generation

```
flask-sqlacodegen --flask --table table "postgresql://user:passwd@host:port/database"
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEzMzQ1MzU1NDJdfQ==
-->