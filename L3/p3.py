#Wapp to read n integers from user and display the count of +ve ,-ve numbers and 0's

import array
data=array.array('i',[ ])
n = int(input("Enter number of elements "))
for i in range(n):
	e = int(input("Enter element "))
	data.append(e)

pc=0
nc=0
zc=0
for i in data:
	if i >0:
		pc=pc+1
	elif i < 0:
		nc=nc+1
	else:
		zc=zc+1
print("+ve no.s ",pc)
print("-ve no.s ",nc)
print("0's ",zc)









