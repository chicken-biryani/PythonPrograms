#Wapp to find sum of digits of the given number by the user (recursively)

def sod(n):
	sum = 0
	if n == 0:
		return 0
	else:
		return n % 10 + sod(n // 10)
	
n = int(input("Enter number ")) 
if n < 0:
	print("b +ve")
else:
	ans = sod(n)
	print("SUM ",ans)
