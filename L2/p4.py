#wapp to read marks (0-100)
# >80-a >60 -b >40 -c
#else d

marks=float(input("enter marks "))

if(marks<0 or marks>100):
	print("invalid marks")
else:
	if(marks>80):
		print("A")
	elif (marks>60):
		print("B")
	elif(marks>40):
		print("C")
	else:
		print("D")
