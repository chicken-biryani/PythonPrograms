#wapp to find maximum of 3 intergers

n1 = int(input("Enter n1 "))
n2 = int(input("Enter n2 "))
n3 = int(input("Enter n3 "))


if n1 > n2:
	max = n1
else:
	max = n2
if n3 > max:
	max = n3
print("max= ",max)