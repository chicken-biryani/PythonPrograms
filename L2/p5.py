#wap to find the sum of first n +ve int
#i/p 3 1+2+3 = 6


num = int(input("enter a +VE number"))
if num < 0:
	print("b +ve")
else:
	i=1
	sum=0
	while i<=num:
		sum=sum+i
		i=i+1
	print("sum is ",sum)