import cx_Oracle

con = None
try:
	con = cx_Oracle.connect("system/abc123")
	print("connected")
	print(con.version)
except cx_Oracle.DatabaseError as e:
	print("Some issue",e)
finally:
	if con is not None:
		con.close()
		print("Disconnected")