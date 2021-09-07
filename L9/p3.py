#wapp to delete a file whose name would be supplied by the user

import os.path
filename = input("Enter file name to delete ")
if os.path.exists(filename):
	os.remove(filename)
	print(filename,"got deleted ")
else:
	print("File doesn't exists!!!!!!!!!!!!!!!!!!!!!!!!!!!  ")
	