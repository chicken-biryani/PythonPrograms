#wap to ad all the numbers in the given csv "2,5,4,8"

str=input("enter the csv")


a=str.split(",")

for i in range(0,len(a),2):
	c=a[i]
	b=int(a[i+1])
	print((c+ " ")*b)
			

