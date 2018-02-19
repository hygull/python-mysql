"""
	{
		"createdOn": "19 FEB 2018",
		"aim": "Inserting user into users table",
		"createdBy": "Rishikesh Agrawani"
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
	version = cursor.fetchone()
except Exception as err:
	print "Error:- ", err
else:
	print "Successfully inserted user into users table"
finally:
	db.close()