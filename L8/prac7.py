#wap to read integr from user and prinft



print("program started")
try:
	num = int(input("enter an integer "))

	print("integer entered",num)
except ValueError:
	print("integer only")
print("program over")
