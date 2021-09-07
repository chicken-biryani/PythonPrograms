#wapp to check if the given number is even/odd


#LOGIC 1:
num = int(input("Enter the number "))
if num % 2 == 0:
	print("even")
else:
	print("odd")

#LOGIC 2:

res = " "
temp = num % 2
if temp ==0:
	res = "Even"
else:
	res = "Odd"
print(res)