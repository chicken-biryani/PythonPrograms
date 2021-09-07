import cx_Oracle

con = None 
cursor = None
try:
	con = cx_Oracle.connect("system/abc123")
	rno = int(input("Enter roll number "))
	name = input("Enter name ")
	cursor = con.cursor()
	sql = "insert into student values('%d' , '%s')"
	args = (rno, name)
	cursor.execute(sql % args)
	con.commit()
	print(cursor.rowcount, " records inserted ")
except cx_Oracle.DatabaseError as e:
	print("some issue ",e)
	con.rollback()
finally:
	if cursor is not None:
		cursor.close()
	if con is not None:
		con.close()
		print("disconnected")