
import array
queue = array.array('i',[ ])

while True:
	option = int(input("1-Insert,2-Remove,3-Peek,4-Display,5-Exit "))
	if option == 1:
		data = int(input("Enter data to insert "))
		queue.append(data)
		print(data, "is Inserted in queue")
	elif option == 2:
		if len(queue) ==0:
			print("Queue is empty")
		else:
			ele =queue.pop(0)
			print(ele," is removed from the queue")
	elif option == 3:
		if len(queue) ==0:
			print("Queue is empty")
		else:
			ele =queue[-1]
			print(ele," is peeked from the queue")	

	elif option == 4:
		if len(queue) ==0:
			print("Queue is empty")
		else:
			print("Queue element ",queue)
	elif option == 5:
		break
	else:
		print("INVALID OPTION/")	








