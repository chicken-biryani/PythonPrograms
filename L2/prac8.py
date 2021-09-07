#reverse the given no.

num = int(input("Enter no "))
if num<0:
	print("b +ve")
else:
	
	rev=0
	while num>0:
		d=num%10
		rev=d + rev*10
		num = num // 10
	else:
		print("Reverse ",rev)