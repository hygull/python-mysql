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