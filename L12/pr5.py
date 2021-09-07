'''wap to create file whosw name would be supllied by user'''

import os.path
file_name-input("enter file name ")
if os.path.exists(file_name):
	print(file_name,"already exists")
else:
	f=none
	try:
		f=open(file_name,"a")
		print(file_name,"created")
	except Exception as e:
		print("creation issue",e)
	finally:
		if f is not None:
			f.close()
		