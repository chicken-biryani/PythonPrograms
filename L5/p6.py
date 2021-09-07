#wapp to read list of marks and find 1.sum 2.average 3.highest 4.lowest

marks = []
ans = input("Do u want to add marks y/n ")
while ans == 'y':
	ele = int(input("Enter Marks "))
	marks.append(ele)
	ans = input("Do u want to add more marks y/n ")
sum = 0
for i in marks:
	sum = sum + i
avg = sum/len(marks)
marks.sort()
print("Sum ",sum,"Avg ",avg)
print("Max ",marks[-1])
print("Min ",marks[0])