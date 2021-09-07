#Wapp to remove even numbers from array
# ar = 35 42 76 33 73
# ar = 35 33 73

import array
data=array.array('i',[ ])
ndata=array.array('i',[ ])
n = int(input("Enter number of elements "))
for i in range(n):
	e = int(input("Enter element "))
	data.append(e)
print(data)
for d in data:
	if d %2!=0:
		ndata.append(d)
print(ndata)









 