''' wapf to find factorial of a number
0! = 1, 1! = 1, 2! = 2, 3! = 6=1*2*3, 4! = 24=1*2*3*4
'''

def fact(n):
	if n==1:
		return 1
	else:
		return n*(n-1)

n = int(input("enter a number "))
if n < 0:
	print("be +ve yaar")
elif n == 0 or n==1:
	print("fact = ", 1)
else:
	ans = fact(n)
	print("fact = ", ans) 