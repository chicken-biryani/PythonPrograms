'''wap to read a string amd count the number of letters
digits '''
lc=dc=oc=0
s1=input("enter A string")

for s in s1:
	if(s.isalpha()):
		lc=lc+1
	elif(s.isdigit()):
		dc=dc+1
	else:
		oc=oc+1
print("letters ",lc,"digits",dc,"others= ",oc)