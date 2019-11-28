## 重命名数据库名
```bash
for table in `mysql -u root -ppassword -s -N -e "use old_db;show tables from old_db;"`; do mysql -u root -ppassword -s -N -e "use old_db;rename table old_db.$table to new_db.$table;"; done;
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEyNjIzNTQwNDNdfQ==
-->