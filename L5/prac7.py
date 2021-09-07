''' 
	wapp7 to read csv and print
eg:	"a,2,d,4,c,3"	
o/p:	a	a
	d	d	d	d
	c	c	c

eg: 	"x,1,y,3"
	x
	y	y	y
'''
s1 = input("enter a correct csv ")
data = s1.split(",")

for i in range(0, len(data), 2):
	what =data[i]
	how =int(data[i+1])
	print(str(what)*how)



















