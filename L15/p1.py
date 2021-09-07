'''wap to connect and dissconect '''

from sqlite3 import *

con=None
try:
	con =  connect("test.db")
	print("connected")
except Exception as e:
	print("insertion issue",e)
finally:
	if con is not None:
		con.close()
		print("dissconected")

