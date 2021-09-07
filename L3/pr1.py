#wap to readd "n: integers from user and
#find and display the coutn if
# 1) number of _+Ve 2) number of -ve 3) no of 0s

import array
data= array.array('i',[])
n= int(input("enter no. of elements"))
for i in range(0,n):
	a=int(input("enter the wlwments"))
	data.append(a)
np,nn,no=0,0,0
for i in data:
	if(i>0):
		np=np+1
	elif(i<0):
		nn=nn+1
	else:
		no=no+1

print("positive",np)
print("negative",nn)
print("zeros",no)