corona={}

while True:
	op = int(input("1- add 2-view 3- update 4-delete and 5-exit"))
	if op==1:
		name = input("enter country name")
		count = corona.get(name,-1)
		if count == -1:
			nopa = int(input("enter number of people"))
			corona[name] = nopa
		else:
			print(name,"already exists")

	elif op == 2:
		print(corona)
	elif op == 3:
		name = input("enter country name")
		count = corona.get(name,-1)
		if count == -1:
			print(name,"does not exists")
		else:
			nopa = int(input("enter number of people"))
			corona[name] = nopa
			

	elif op == 4:
		name = input("enter country name")
		count = corona.get(name,-1)
		if count == -1:
			print(name,"does not exists")
		else:
			del corona[name]
		
	elif op == 5:
		break
	else:
		print("invalid option")