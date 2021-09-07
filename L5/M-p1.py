#waPF to check & return True/False whether the given number is Armstrong Number

def armstrong(n):
	sum = 0
	c = 0
	while(n>0):
		c=c+1
		n = n // 10
	while (n>0):
		digit = n % 10
		sum = sum + digit ** c
		n = n // 10
	return sum

n = int(input("Enter no "))
temp = n
ans = armstrong(n)

if(ans == temp):                 
	print("Armstrong Number ")
else:
	print("Not Armstrong Number")
