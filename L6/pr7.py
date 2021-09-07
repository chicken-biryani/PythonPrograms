''' 
wapf to find the sum of the digits
i/p: 	354	o/p: 12
i/p: 	1234	o/p: 10
'''

def sod(n):
	if n==0:
		return n
	else:
		return n%10+sod(n//10)

num = int(input("enter a number "))
if num < 0:
	print("b+ve")
else:
	ans = sod(num)
	print("sum = ", ans)

