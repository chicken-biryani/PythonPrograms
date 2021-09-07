#wap to read ltuple of int from user
#and dispaly on the screen
list_data=[]
tuple_data=()
reply = input("do u want to add some integers y/n")
while reply == 'y':
	ele = int(input("enter element"))
	list_data.append(ele)
	reply = input("do u want to add some more integers y/n")

tuple_data=tuple(list_data)

print(tuple_data)
list_data.sort(reverse=True)
tuple_data=tuple(list_data)

print(tuple_data)
