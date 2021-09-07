#wap to read marks and print highest  marks

marks=[]
reply = input("do u want to enters marks of students  y/n ")
while reply == 'y':
	ele = float(input("enter mrks "))
	marks.append(ele)
	reply = input("do u want to add some more students  marks y/n ")

print(marks)


marks.sort() 
print("highest",marks[-1])
print("lowest",marks[0])
