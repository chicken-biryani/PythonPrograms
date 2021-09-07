num = int(input("enter a number"))

if num < 0:
	print("b +ve")
else:
	a=10
	for i in range(num,0,-1):
		print(i*(str(a)+"\t"))
		a=a+10
	
