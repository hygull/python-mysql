# python-mysql

MySQL database connectivity using Python.

### System 

Windows 10 pro, 64-bit

### Python version

Python 2.7.14 :: Anaconda, Inc.(64-bit)

### MySQL version

MySQL 5.7.21

```
rishikesh agrawani@DESKTOP-8AATOO4 MINGW64 /d/projects/Python/MySQL (master)
$ python --version
Python 2.7.14 :: Anaconda, Inc.

rishikesh agrawani@DESKTOP-8AATOO4 MINGW64 /d/projects/Python/MySQL (master)
$ python -c "import os; print os.system('python --version')"
Python 2.7.14 :: Anaconda, Inc.
0

rishikesh agrawani@DESKTOP-8AATOO4 MINGW64 /d/projects/Python/MySQL (master)
$ mysql --version
D:\projects\MySQL\mysql-5.7.21-winx64\mysql-5.7.21-winx64\bin\mysql.exe  Ver 14.14 Distrib 5.7.21, for Win64 (x86_64)

```

### MySQL-python 1.2.3 for Windows and Python 2.7, 32bit and 64bit versions

Visit [http://www.codegood.com/archives/129](http://www.codegood.com/archives/129) and download [MySQL-python-1.2.3.win-amd64-py2.7.exe](MySQL-python-1.2.3.win-amd64-py2.7.exe) as I have 64-bit Python 2.7.14.

If you have 32-bit Python installed then you will need to download and install 
[MySQL-python-1.2.3.win32-py2.7.exe](MySQL-python-1.2.3.win32-py2.7.exe).

If you want different versions then you can visit [http://www.codegood.com/downloads](http://www.codegood.com/downloads) and download according to your choice.

Install it as it is required for installing MySQLdb package of Python.

### Still I'm facing problems

Still you can face problems while running Python programs using `MySQLdb` package if your Windows OS is missing some `dll files`. 

I was facing the issue because my Windows machine was not having `MSVCR120.dll` 
 & `MSVCP120.dll.` files. I downloaded these from [http://www.dlldownloader.com/msvcr120-dll/](http://www.dlldownloader.com/msvcr120-dll/) page and [http://www.dlldownloader.com/msvcp120-dll/](http://www.dlldownloader.com/msvcp120-dll/) respectively & installed.

Now I was ok/satisfied with my System setup and requirements. So let us move now.

### Getting started

Create any directory named `examples` and navigate inside that.

Create `config.py` and paste the following then update the credentials.

```python
HOST = "127.0.0.1"

PORT = "3306"

USER = "rishikesh"

PASSWORD = "rishikesh@321"

DATABASE = "nodejs"

``` 

Create `01_connection.py` and paste the following code.

```python
"""
	{
		"createdOn": "17 FEB 2018",
		"aim": "Connecting to MySQL database",
		"createdBy": "Rishikesh Agrawani"
	}
"""

import MySQLdb
import config

try:
	connection_config = [config.HOST, config.USER, config.PASSWORD, config.DATABASE]

	db = MySQLdb.connect(*connection_config)
	cursor = db.cursor()

	query = "SELECT VERSION();";

	cursor.execute(query)
	version = cursor.fetchone()
except Exception as err:
	print "Error:- ", err
else:
	print version[0] # ('5.7.21',)
	print type(version[0]) # <type 'str'>
	print "Successfully connected to DATABASE"
finally:
	db.close()

```

Run `01_connection.py` as follows as I ran using GIT bash terminal.

```bash
rishikesh agrawani@DESKTOP-8AATOO4 MINGW64 /d/projects/Python/MySQL/examples (master)
$ python 01_connection.py
5.7.21
<type 'str'>
Successfully connected to DATABASE

```

Now lets try another example related to getting/extracting table data.

Make sure you have `nodejs` database and `users` table with follwing table structure.

```mysql
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| nodejs             |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.02 sec)

mysql> use nodejs
Database changed
mysql> show tables;
+------------------+
| Tables_in_nodejs |
+------------------+
| posts            |
| users            |
+------------------+
2 rows in set (0.00 sec)

mysql> DESC users;
+------------+-------------+------+-----+-------------------+-----------------------------+
| Field      | Type        | Null | Key | Default           | Extra                       |
+------------+-------------+------+-----+-------------------+-----------------------------+
| id         | bigint(20)  | NO   | PRI | NULL              | auto_increment              |
| fullname   | varchar(50) | NO   |     | NULL              |                             |
| email      | text        | NO   |     | NULL              |                             |
| contact    | varchar(10) | NO   |     | NULL              |                             |
| address    | text        | YES  |     | NULL              |                             |
| password   | varchar(20) | NO   |     | NULL              |                             |
| created_at | timestamp   | NO   |     | CURRENT_TIMESTAMP |                             |
| updated_at | timestamp   | NO   |     | CURRENT_TIMESTAMP | on update CURRENT_TIMESTAMP |
+------------+-------------+------+-----+-------------------+-----------------------------+
8 rows in set (0.00 sec)

mysql> SELECT * FROM `users`;
+----+------------------+----------------------------+------------+------------------+--------------+---------------------+---------------------+
| id | fullname         | email                      | contact    | address          | password     | created_at          | updated_at          |
+----+------------------+----------------------------+------------+------------------+--------------+---------------------+---------------------+
|  1 | Rob Pike         | rob.pike@gmail.com         | 8787676554 | Nagpur, INDIA    | rob@321      | 2018-02-11 18:38:58 | 2018-02-17 17:12:56 |
|  2 | Robert Griesemer | robert.griesemer@gmail.com | 8988007656 | Gurgaon, INDIA   | robert@321   | 2018-02-17 16:44:30 | 2018-02-17 16:44:30 |
|  3 | Ken Thompson     | ken.thompson@gmail.com     | 8988007455 | Bangalore, INDIA | ken@321      | 2018-02-17 16:45:43 | 2018-02-17 16:45:43 |
|  4 | Tkinter Tk       | tkinter.tk@gmail.com       | 8934567455 | Bilaspur, INDIA  | tkinter@321  | 2018-02-17 16:47:12 | 2018-02-17 16:47:12 |
|  5 | MySQL Db         | mysql.db@gmail.com         | 8754567445 | Mysore, INDIA    | mysql.db@321 | 2018-02-17 16:48:38 | 2018-02-17 16:48:38 |
+----+------------------+----------------------------+------------+------------------+--------------+---------------------+---------------------+
5 rows in set (0.00 sec)

mysql>

```

Now create another file named `02_get_users.py` and paste the below code.

```python
"""
	{
		"createdOn": "17 FEB 2018",
		"aim": "Connecting to MySQL database and getting users",
		"createdBy": "Rishikesh Agrawani"
	}
"""

import MySQLdb
import config

try:
	connection_config = [config.HOST, config.USER, config.PASSWORD, config.DATABASE]

	db = MySQLdb.connect(*connection_config)
	cursor = db.cursor()

	query = "SELECT * FROM `users`";

	cursor.execute(query)
	rows = cursor.fetchall()

	row1 = None
	shore = "+-" + "-"*30 + "-+"
	for row in rows:
		if not row1:
			row1 = row
		print shore
		print "| %-30s |" % row[2]
	print shore

	print str(len(row1)) + " columns"
except Exception as err:
	print "Error:- ", err
else:
	print "Successfully fetched users from MySQL DATABASE"
finally:
	db.close()

```

Finally execute the code as I executed using GIT bash as follows.

```
rishikesh agrawani@DESKTOP-8AATOO4 MINGW64 /d/projects/Python/MySQL/examples (master)
$ ls
01_connection.py  02_get_users.py  config.py  config.pyc

rishikesh agrawani@DESKTOP-8AATOO4 MINGW64 /d/projects/Python/MySQL/examples (master)
$ python 02_get_users.py
+--------------------------------+
| rob.pike@gmail.com             |
+--------------------------------+
| robert.griesemer@gmail.com     |
+--------------------------------+
| ken.thompson@gmail.com         |
+--------------------------------+
| tkinter.tk@gmail.com           |
+--------------------------------+
| mysql.db@gmail.com             |
+--------------------------------+
8 columns
Successfully fetched users from MySQL DATABASE

```

Let us insert 1 more record into the `users` table.

Create a file named `03_insert_user.py` and paste the below code on it.

```python
"""
	{
		"createdOn": "19 FEB 2018",
		"aim": "Inserting user into users table",
		"createdBy": "Rishikesh Agrawani",
		"note": "Do not forget to commit"
	}
"""
import MySQLdb
import config

try:
	connection_config = [config.HOST, config.USER, config.PASSWORD, \
		config.DATABASE
	]

	db = MySQLdb.connect(*connection_config)
	cursor = db.cursor()

	query = "INSERT INTO `users` (fullname, email, contact, address, password \
		) VALUES ('Hemkesh Agrawani', 'hemkesh.agrawani@gmail.com', '7898869706', 'Raipur, CG', 'hemkesh@321')";

	cursor.execute(query)
	db.commit()
except Exception as err:
	print "Error:- ", err
	db.rollback()
else:
	print "Successfully inserted user into users table"
finally:
	db.close()

```

After running the above code I got the o/p as follows on Terminal.

```bash
rishikesh agrawani@DESKTOP-8AATOO4 MINGW64 /d/projects/Python/MySQL/examples (master)
$ python 03_insert_user.py
Successfully inserted user into users table

rishikesh agrawani@DESKTOP-8AATOO4 MINGW64 /d/projects/Python/MySQL/examples (master)
$ python 02_get_users.py
+--------------------------------+
| rob.pike@gmail.com             |
+--------------------------------+
| robert.griesemer@gmail.com     |
+--------------------------------+
| ken.thompson@gmail.com         |
+--------------------------------+
| tkinter.tk@gmail.com           |
+--------------------------------+
| mysql.db@gmail.com             |
+--------------------------------+
| hemkesh.agrawani@gmail.com     |
+--------------------------------+
8 columns
Successfully fetched users from MySQL DATABASE

```

Enjoy more examples related to `post`/`INSERT`, `get`/`SELECT`, `put`/`UPDATE`, `delete`/`DELETE` etc. and many other operations.


