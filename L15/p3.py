from sqlite3 import *

con=None

try:
	con=connect("test.db")
	print("connected")
	cursor=con.cursor()
	sql="insert into student values(10,'amit')"
	cursor.execute(sql)
	con.commit()
	print("record added")
except Exception as e:
	print("insertion issue",e)
	con.rollback()
finally:
	if con is not None:
		con.close()
		print("disconnected")
	