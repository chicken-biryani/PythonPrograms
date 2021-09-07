#wapp to read list of animal names & find the longest names

names= [] 
ans = input("Do u want to add name y/n ")
while ans == 'y':
	ele = input("Enter name ")
	names.append(ele)
	ans = input("Do u want to add more names y/n ")
max = len(names[0])
for n in names:
	if len(n) > max:
		msx = len(n)
for n in names:
	if len(n) == max:
		print(n)
 
	
