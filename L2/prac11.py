#pattern
r = int(input("Enter no. of rows "))
if r < 0:
	print("b +ve")
else:
	ch = 65
	for i in range(1,r+1):
		print( ( str(chr(ch)) + "\t" ) * i)
		ch=ch+1
