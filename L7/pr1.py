''' wapf to check if the given number is Armstrong Number 
	eg:  	pqr = p^3 + q^3 + r^3
		153 = 1^3 + 5^3 + 3^3
		370 = 3^3 + 7^3 + 0^3
	
	eg:	abcd = a^4 + b^4 + c^4 + d^4
'''

def check(num):
	org_num = num
	sum = 0
	while num!=0:
		digit =num%10
		sum = sum+ digit**3
		num =num//10
	if org_num == sum:
		return True
	else:
		return False
num = int(input("enter a number "))
if num < 0:
	print("be positive")
elif check(num):
	print("amstrong")
else:
	print("not an amstrong")










