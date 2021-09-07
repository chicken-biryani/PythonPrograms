import cx_Oracle

con = None 
cursor = None
try:
	con = cx_Oracle.connect("system/abc123")
	rno = int(input("Enter roll number "))
	name = input("Enter name ")
	cursor = con.cursor()
	sql = "select * from student"
	cursor.execute(sql)
	data = cursor.fetchall()
	for d in data:
		print("rno" ,d[0]," name ",d[1] )
except cx_Oracle.DatabaseError as e:
	print("some issue ",e)
	con.rollback()
finally:
	if cursor is not None:
		cursor.close()
	if con is not None:
		con.close()
		print("disconnected")