#wapp to read list of integers and create two lists even_list & odd_ list
even_data,odd_data = [], []
data = []
ans = input("Do u want to add elements y/n ")
while ans == 'y':
	ele = int(input("Enter element "))
	data.append(ele)
	ans = input("Do u want to add more elements y/n ")
for i in data:
	if(i%2==0):
		even_data.append(i)
	else:
		odd_data.append(i)

print(data)
print(even_data)
print(odd_data)