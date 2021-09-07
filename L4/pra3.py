num = int(input("enter a number"))

if num < 0:
	print("b +ve")
else:
	for i in range(num,0,-1):
		print(i*("*"+"\t"))
	
