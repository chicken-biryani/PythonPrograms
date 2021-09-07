''' wapp6 to read csv  string which contains numbers and add the numbers
i/p: "10,30,20"		o/p:  60 '''

s1 = input("enter csv string ")
data =s1.split(',')

sum = 0
for d in data:
	if d.isdigit():
		sum = sum+int(d)

print("sum = ", sum)

