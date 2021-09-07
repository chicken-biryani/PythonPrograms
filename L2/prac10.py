#pattern
r = int(input("Enter no. of rows "))
if r < 0:
	print("b +ve")
else:
	
	for i in range(1,r+1):
		print("* " * i)
