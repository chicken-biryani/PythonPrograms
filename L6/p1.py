#wapp to read a tuple of integers from a user and sort in descending order

list1 = []
tup1 = ()
	
ans = input("Do you want to add integers y/n ")
while ans == "y":
	n = int(input("Enter Integer "))
	list1.append(n)
	ans = input("Do you want to add more integers y/n ")
tup1 = tuple(list1)
print(tup1)

list1.sort(reverse = True)

tup1 = tuple(list1)
print(tup1)
