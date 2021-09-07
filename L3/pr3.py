#wap LIFO FIFO

import array

q = array.array('i',[])

while True:
	op= int(input("1-insert 2-remove 3-peek 4-display 5-exit"))
	if op==1:
		ele=int(input("enter the elem "))
		q.append(ele)
	elif op==2:
		if len(q)==0:
			print("empty queue")
		else:
			e=q.pop(0)
			print("popped element if",e)

	elif op==3:
		if len(q)==0:
			print("empty queue")
		else:
			print(" element is",q[-1])

	elif op==4:
		if len(q)==0:
			print("empty queue")
		else:
			print(" elements are",q)
	elif op==5:
		break
	else:
		print("invalid")
				