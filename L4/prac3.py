#sum of digits

def sod(num):
	sum=0
	while num>0:
		digit = num%10
		sum=sum+digit
		num=num//10
	return sum

number= int(input("enter number"))

if number <0:
	print("be positive")
else:
	print(sod(number))