#Wapp to find sum of digits of the given number by the user (non-recursively)

def sod(n):
	sum = 0
	while(n > 0):
		d = n % 10
		sum = sum + d
		n = n//10
	return sum
	
n = int(input("Enter number ")) 
if n < 0:
	print("b +ve")
else:
	ans = sod(n)
	print("SUM ",ans)
