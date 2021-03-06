from mysql.connector import MySQLConnection, Error
from SQL02dbconfig import read_db_config

def connect():
	db_config = read_db_config()
	
	try:
		print('Connecting to MySQL database...')
		conn = MySQLConnection(**db_config)
		
		if conn.is_connected():
			print('Connection estabilished.')
		else:
			print('Connection failed.')
	
	except Error as error:
		print(error)
		
	finally:
		conn.close()
		print('Connection closed.')

if __name__ == '__main__':
	connect()