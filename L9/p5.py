import os.path
filename = input("Enter file name to read from ")
if os.path.exists(filename):
	f = None
	try:
		f = open(filename)
		data = f.read()
		print("data from file: ",data)

	except Exception as e:
		print(e)
	finally:
		if f is not None:
			f.close()
else:
	print(filename," doesn't exists ")