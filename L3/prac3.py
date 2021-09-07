

n = int(input("enter +ve integer "))
if n < 0 :
	print("b +ve")
else:
	sum =0
	a=n
	while n !=0:
		digit = n%10
		sum = sum+digit
		n=n//10
	
print("sum = ", sum)