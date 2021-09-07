#wapp to read list of names and create new list which does not contain duplicate names.

names,new_names = [] ,[]
ans = input("Do u want to add name y/n ")
while ans == 'y':
	ele = input("Enter name ")
	names.append(ele)
	ans = input("Do u want to add more names y/n ")
for i in names:
	if i not in new_names:
		new_names.append(i)

print("Original ", names)
print("new ",new_names)	