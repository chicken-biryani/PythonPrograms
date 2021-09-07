#wapp to find factorial of a given no.

num = int(input("Enter a number "))
if num < 0:
	print("b +ve")
else:
	fact = 1
	for i in range(1,num+1):
		fact = fact*i
	print("Fact= ",fact)
