#wapp to count the no.of vowels & consonants
#eg i/p- pinnacle   o/p vc=3 cc=5
#eg i/p-kamal classes o/p vc = 4 cc=8

s1=input("Enter a String ")

vc=0
cc=0

for s in s1:
	if s.isalpha():
		if s in ['a' , 'e' , 'i' , 'o' , 'u' , 'A' , 'E' , 'I' ,'O' , 'U' ]: 
			vc = vc + 1
		else:
			cc = cc + 1
print("Vc = ",vc," Cc = ", cc)