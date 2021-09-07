#waPF to check & return True/False whether the given number is Armstrong Number

def check(n):
	temp = n
	sum = 0
	while (n>0):
		digit = n % 10
		sum = sum + digit **4
		n = n // 10
	if (sum == temp):
		return True
	else:
		return False

for i in range(1000,10000):
	if check(i):
		print(i)