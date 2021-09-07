'''wap2  to create table studest c1-rno c-student '''

from sqlite3 import *

con=None

try:
	con=connect("test.db")
	print("connected")
	cursor=con.cursor()
	sql="create table student(rno int primary key,name text)"
	cursor.execute(sql)
	print("table created")
except Exception as e:
	print("issue",e)
finally:
	if con is not None:
		con.close()
		print("disconnected")
	