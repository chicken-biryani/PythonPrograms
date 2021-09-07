'''wapp to count the number of letters,digits & other characters
    eg:- i/p: k@m@l123l
           o/p: lc=3 dc=3 oc=3'''

s1=input("Enter a String ")

lc=0
dc=0
oc=0

for s in s1:
	if s.isalpha( ):
		lc=lc+1
	elif s.isdigit( ):
		dc=dc+1
	else:
		oc=oc+1
print("lc = ",lc," dc = ", dc," oc = ",oc)







 