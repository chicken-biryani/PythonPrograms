n = int(input("enter +ve integer "))
if n < 0 :
	print("b +ve")
else:
	rev =0
	a=n
	while n !=0:
		digit = n%10
		rev = rev*10+digit
		n=n//10
	
print("rev is ", rev)

for i in range(-2):
	print(i)