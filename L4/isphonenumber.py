#regular expression


def isphonenumber(a):
	if(len(a)!=12):
		return False
	elif(a.find('-')!=3 and a.rfind('-')!=7 ):
		return False
	elif(a[:3].isdigit() and a[4:7].isdigit() and a[8:11].isdigit() ):
		return True
	else:
		return False

print(isphonenumber('111-111-1111'))


b=input("enter string ")
for i in range (len(b)):
	chunk=b[i:i+12]
	if(isphonenumber(chunk)):
		print(chunk)