#wap to read list  of int from user
#and dispaly on the screen



data=[]
reply = input("do u want to add some integers y/n ")
while reply == 'y':
	ele = int(input("enter element "))
	data.append(ele)
	reply = input("do u want to add some more integers y/n ")

print(data)

for d in data:
	print(d, end=' ')
print()