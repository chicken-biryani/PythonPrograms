'''wap to read from an existing file'''

import os.path
 
file_name = input("enter file name to read from ")
if os.path.isfile(file_name):
	f = None
	try:
		with open(file_name,'r') as f:
			data=f.read()
			print(data)
	except Exception as e:
		priny("read issue")
else:
	print(file_name,"does not exist")