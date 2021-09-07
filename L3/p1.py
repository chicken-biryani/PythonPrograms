#Wapp to read array elements from the user and display on screen 

import array
data = array.array('i', [ ])
n = int(input("Enter number of elements "))
for i in range(n):
	ele = int(input("Enter element "))
	data.append(ele)

print(data)
for d in data:
	print(d, end=' ')
print()
for i in range(len(data)):
	print(data[i],end=' ')
print()


