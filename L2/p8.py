#wapp to find the factorial a number


num = int (input("enter a number"))
if num<0:
	print("b +ve")
elif num == 0 or num == 1:
	print("fact= ",1)
else:
	fact = 1
	for i in range(1,num+1):
		fact=fact*i
	print("fact= ", fact)