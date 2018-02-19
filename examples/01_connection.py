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