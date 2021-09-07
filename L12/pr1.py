'''wap to read integer and print yes if user provides  integer else no'''

try:
	a=int(input("enter number "))
	print("yes")

except ValueError:
	print("no")