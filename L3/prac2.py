# wapp1 to find the sum of first 'n' +ve integers
# n=5	1+2+3+4+5 = 15
# n=3	1+2+3 = 6

n = int(input("enter +ve integer "))
if n < 0 :
	print("b +ve")
else:
	sum =0
	i = 1
	while i<=n     :
		sum = sum+i
		i = i + 1
	else:
	print("sum = ", sum)