#copy file

import os.path
src_filename = input("Enter source filename  ")
if os.path.exists(src_filename):
	dest_filename = input("Enter destinn filename ")
	if os.path.exists(dest_filename):
		print(dest_filename," already exists ")
	else:
		f1 = open(src_filename,"r")
		f2 = open(dest_filename,"w")
		data = f1.read()
		f2.write(data)
		print("copy completed ")
		f1.close()
		f2.close()
else:
	print(src_filename , "doesn't exists ")