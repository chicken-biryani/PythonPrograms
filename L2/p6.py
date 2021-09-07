#wapp to find the sum of the digits

num=int(input("enter the number"))
if num<0:
	print("invalid")
else:
	a=num
	sum=0
	while(num>0):
		sum=sum+num%10
		num=num//10
	print("the sum is",sum)	