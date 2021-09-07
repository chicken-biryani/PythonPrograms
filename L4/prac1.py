#wap to find fact of number



#using non recursive
def fact(num):
	f=1
	for i in range(1,num+1):
		f=f*i
	return f


number =int(input("enter number  "))

if number<0:
	print("enter a positive number ")
elif number==0 or number==1:
	print("1")
else:
	ans = fact(number)
	print("fact ",ans)

#first define then call else name error
