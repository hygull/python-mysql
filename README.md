# python-mysql

MySQL database connectivity using Python.

### System 

Windows 10 pro, 64-bit

### Python version

Python 2.7.14 :: Anaconda, Inc.

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

Visit [http://www.codegood.com/archives/129](http://www.codegood.com/archives/129) and download [MySQL-python-1.2.3.win-amd64-py2.7.exe](MySQL-python-1.2.3.win-amd64-py2.7.exe).

Install it as it is required for installing MySQLdb package of Python.

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

Run `01_connection.py` using the below command.

```python
python 01_connection.py
```

