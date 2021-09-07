def sod(num):
	if(num==0):
		return 0
	else:	
		return num%10+sod(num//10)

		

number= int(input("enter number"))


if number <0:
	print("be positive")
else:
	print(sod(number))
