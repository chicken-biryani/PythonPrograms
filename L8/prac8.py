#wap to read integr from user and prinft



print("program started")
try:
	num = int(input("enter  integer 1 "))
	num2 = int(input("enter  integer 2 "))
	print(num/num2)
except ValueError:
	print("integer only")
except ZeroDivisionError:
	print("second num cant be 0")
else:
	print("ans ",ans) #will run only when the try block will run
print("program over")