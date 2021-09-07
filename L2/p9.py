#wapp to find the patter

a= int(input("enter num of rows"))



for i in range (1,a+2):
	for j in range(1,i):
		print("*",end=' ')
	print()
#that was my way

#sirs method
for i in range(1,a+1):
	print(i* ("*" + "\t"))
	
#yeh multiplication 

for i in range(1,a+1):
	print(i* (chr(i+65-1) + "\t")) #gives characeter equivalent of unicode value
print()
print()
for i in range(a,0,-1):
	print(i* ("*" + "\t"))
ch=97
for i in range(a,0,-1):
	
	print(i* (chr(ch) + "\t"))
	ch=ch+1