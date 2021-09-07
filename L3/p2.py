#Wapp to read marks from user of n students & find
#1.sum of marks
#2.avg marks
#3.highest marks
#4.lowest marks

import array
marks = array.array('i' , [ ])
n = int(input("Enter number of Students "))
for i in range(n):
	m = int(input("Enter Marks "))
	marks.append(m)
sorted(marks)
sum=0
for m in marks:
	sum = sum + m
avg = sum / n
print("Sum of all marks ",sum)
print("Avg of marks ",avg)
print("avg = %.2f" %avg)
print("Highest marks ",marks[n-1])
print("Lowest marks ",marks[0])


max = marks[0]
min = marks[0]

for m in marks:
	if m > max :
		max = m
	if m < min:
		min = m

print("min = ",min)
print("max = ",max)

