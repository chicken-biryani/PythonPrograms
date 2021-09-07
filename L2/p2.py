#wap to take amount from user if amt is +ve and >129 then 10% disc



num=int(input("enter the number"))
if num<0:
	print("invalid")
else:
	a=num
	sum=0
	while(num>0):
		sum=sum*10+num%10
		num=num//10
	else:
		print("the sum is",sum)	

