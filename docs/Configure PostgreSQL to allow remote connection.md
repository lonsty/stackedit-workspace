> [https://blog.bigbinary.com/2016/01/23/configure-postgresql-to-allow-remote-connection.html](https://blog.bigbinary.com/2016/01/23/configure-postgresql-to-allow-remote-connection.html)

# Configure PostgreSQL to allow remote connection

By default PostgreSQL is configured to be bound to `localhost`.

	$ netstat -nlt
	Proto Recv-Q Send-Q Local Address           Foreign Address         State
	tcp        0      0 0.0.0.0:443             0.0.0.0:*               LISTEN
	tcp        0      0 127.0.0.1:11211         0.0.0.0:*               LISTEN
	tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN
	tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN
	tcp        0      0 127.0.0.1:5432          0.0.0.0:*               LISTEN
	tcp        0      0 127.0.0.1:3737          0.0.0.0:*               LISTEN
	tcp6       0      0 :::22                   :::*                    LISTEN

As we can see above port  `5432`  is bound to  `127.0.0.1`. It means any attempt to connect to the postgresql server from outside the machine will be refused. We can try hitting the port  `5432`  by using telnet.

	$ telnet 107.170.11.79 5432
	Trying 107.170.11.79...
	telnet: connect to address 107.170.11.79: Connection refused
	telnet: Unable to connect to remote host

## Configuring postgresql.conf

In order to fix this issue we need to find  `postgresql.conf`. In different systems it is located at different place. I usually search for it.

	$ find / -name "postgresql.conf"
	/var/lib/pgsql/9.4/data/postgresql.conf

Open  `postgresql.conf`  file and replace line

	listen_addresses = 'localhost'

with

	listen_addresses = '*'

Now restart postgresql server.

	$ netstat -nlt
	Proto Recv-Q Send-Q Local Address           Foreign Address         State
	tcp        0      0 127.0.0.1:11211         0.0.0.0:*               LISTEN
	tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN
	tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN
	tcp        0      0 0.0.0.0:5432            0.0.0.0:*               LISTEN
	tcp        0      0 127.0.0.1:25            0.0.0.0:*               LISTEN
	tcp        0      0 127.0.0.1:2812          0.0.0.0:*               LISTEN
	tcp6       0      0 ::1:11211               :::*                    LISTEN
	tcp6       0      0 :::22                   :::*                    LISTEN
	tcp6       0      0 :::5432                 :::*                    LISTEN
	tcp6       0      0 ::1:25                  :::*                    LISTEN

Here we can see that “Local Address” for port  `5432`  has changed to  `0.0.0.0`.

## Configuring pg_hba.conf

Let’s try to connect to remote postgresql server using “psql”.
	
	$ psql -h 107.170.158.89 -U postgres
	psql: could not connect to server: Connection refused
		Is the server running on host "107.170.158.89" and accepting
		TCP/IP connections on port 5432?

In order to fix it, open  `pg_hba.conf`  and add following entry at the very end.

	host    all             all              0.0.0.0/0                       md5
	host    all             all              ::/0                            md5

The second entry is for IPv6 network.

Do not get confused by “md5” option mentioned above. All it means is that a password needs to be provided. If you want client to allow collection without providing any password then change “md5” to “trust” and that will allow connection unconditionally.

Restart postgresql server.

	$ psql -h 107.170.158.89 -U postgres
	Password for user postgres:
	psql (9.4.1, server 9.4.5)
	Type "help" for help.

	postgres=# \l

You should be able to see list of databases.

Now we are able to connect to postgresql server remotely.

Please note that in the real world you should be using extra layer of security by using “iptables”.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTY5NjU2NDU5MF19
-->