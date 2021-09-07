#wap amstrong


def check(num,b):
	sum=0
	while(num>0):
		digit=num%10
		sum=sum+pow(digit,b)
		num=num//10
	return sum





a=input("enter number")
b=len(a)
num=int(a)

c=check(num,b)

if(c==num):
	print("amstrong")
else:
	print(" notamstrong")

