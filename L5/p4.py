'''wapp to read list of integers from the iser
    and rint on the screen '''
data = []
ans = input("Do u want to add elements y/n ")
while ans == 'y':
	ele = int(input("Enter element "))
	data.append(ele)
	ans = input("Do u want to add more elements y/n ")
print(data)
for d in data:
	print(d, end = ' ')
print()
for i in range(len(data)):
	print(data[i], end = ' ')
print()