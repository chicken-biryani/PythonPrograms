#wapp to find sum of digits 

num = int(input("Enter number "))

if num <0:
	print("b+ve")
else:
	sum=0
	while num > 0:
		digit = num%10 
		sum= sum + digit
		num=num//10
	else:
		print("sum = ",sum)