#wapp to write a data into file

import os.path
filename = input("Enter file name to write ")
if os.path.exists(filename):
	f = None
	try:
		f = open(filename , "a")
		data = input("Enter data to write ")
		f.write(data + "\n")
	except Exception as e:
		print("some issues ",e)
	finally:
		if f is not None:
			f.close()
	
else:
	print(filename , "doesn't exists ")
	