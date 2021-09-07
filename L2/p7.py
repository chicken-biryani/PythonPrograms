#wap to take amount from user if amt is +ve and >129 then 10% disc



num=int(input("enter the number"))
if num<0:
	print("invalid")
else:
	a=num
	rev=0
	while(num>0):
		rev=rev*10+num%10
		num=num//10
	else:
		print("the reverse is ",rev)	 
"""while ka else jab pura while execute hoga tabhi yeh else execute karna warna mat karna"""

