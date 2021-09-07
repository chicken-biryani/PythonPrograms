num = int(input("enter a number"))

if num < 0:
	print("b +ve")
else:
	for i in range(1,num+1):
		print(i*(str(i)+"\t"))