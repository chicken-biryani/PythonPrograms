#wap lower,upper,digit,other


string =input("enter a string")
lc=uc=dc=oc=0
for s in string:
	if 'a'<= s <='z':
		lc=lc+1
	elif 'A'<= s <='Z':
		uc=uc+1
	elif '1'<= s <='9':
		dc=dc+1
	else:
		oc=oc+1

print("upper - " ,uc," lower ",lc, "digit ",dc,"other",oc) 

string =input("enter a string")
lc=uc=dc=oc=0
for s in string:
	if s.islower():
		lc=lc+1
	elif s.isupper():
		uc=uc+1
	elif s.isdigit():
		dc=dc+1
	else:
		oc=oc+1
print("upper - " ,uc," lower ",lc, "digit ",dc,"other",oc) 
