#wapp to read two intergers from user and perform ans = a/b

print("program execution started ")
try:
	a = int(input("Enter 1st no "))
	b = int(input("Enter 2nd no "))
	ans = a/b
except ValueError:
	print("both shud be integers ")
except ZeroDivisionError:
	print("2nd number should not be 0 ")
else:
	print("Ans = ", ans)
finally:
	print("program execution ended")
















