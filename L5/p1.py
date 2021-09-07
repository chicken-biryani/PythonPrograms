#waPF to check & return True/False whether the given number is Armstrong Number

def check(n):
	temp = n
	sum = 0
	while (n>0):
		digit = n % 10
		sum = sum + digit **3
		n = n // 10
	if (sum == temp):
		return True
	else:
		return False
n = int(input("Enter no "))

if n < 0:
	print("b+ve")
elif check(n):
	print("Armstrong Number ")
else:
	print("Not Armstrong Number")
