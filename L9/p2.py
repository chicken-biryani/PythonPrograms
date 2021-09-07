#wapp to create a file whose name would be given by the user

import os.path
filename = input("Enter file name to create ")
if os.path.exists(filename):
	print(filename, "already exists ")
else:
	f = open(filename , "a")
	print(filename , "got created")
	f.close()
