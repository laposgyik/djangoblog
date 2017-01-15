from mysql.connector import MySQLConnection, Error
from SQL02dbconfig import read_db_config

def insert_table(firstN, secN, city, adress):
	query = "INSERT INTO Persons(firstN, secN, city, adress) VALUES(%s,%s,%s,%s)"
	args = (firstN, secN, city, adress)
	
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)
		
		cursor = conn.cursor()
		cursor.execute(query, args)
		
		if cursor.lastrowid:
			print('last insert id:', cursor.lastrowid)
		else:
			print('last insert id not found')
			
			conn.commit()
	
	except Error as e:
		print(e)
	
	finally:
		cursor.close()
		conn.close()
		
if __name__ == '__main__':
	insert_table('Toth', 'Otto', 'London', 'Funky street 12375')