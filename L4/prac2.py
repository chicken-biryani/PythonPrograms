#using recurrsion
def fact(num):
	if num==1:
		return 0
	else:
		return num*fact(num-1)

number= int(input("enter number"))
if number<0:
	print("nikal")
elif number==0 or number==1:
	print("1")
else:
	ans = fact(number)
	print("fact ",ans)

#first define then call else name error
