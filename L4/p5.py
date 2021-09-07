'''wapp to read a string and create new string that would not 
    contain any vowels
    i/p:- kamal classes o/p:- kml clsss
    i/p:- pinnacle  o/p:- pnncl'''

s1 = input("Enter a String ")
ns1 = " "
for s in s1:
	if s.isalpha():
		if s not in ['a' , 'e' , 'i' , 'o' , 'u' , 'A' , 'E' , 'I' ,'O' , 'U' ]: 
			ns1 = ns1 + s
print("Original ",s1,"New ",ns1)	
			
	