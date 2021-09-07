f=None

try:
	f=open("abc.txt",r)
	data=f.read()
	print(data)
except FileNotFoundError:
	print("check file name")
finally:
	if f is not None:
		f.close()