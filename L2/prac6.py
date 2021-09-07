#wapp to find the sum of first n positive numbers
#i/p: 5: 	1 + 2 + 3 + 4 + 5 = 15

num = int(input("Enter positive number "))
if num < 0:
	print("b +ve")
else:
	i = 1
	sum = 0
	while i <= num:
		sum = sum + i
		i = i +1
	print("sum = ",sum)