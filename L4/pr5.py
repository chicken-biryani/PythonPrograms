#wap modify pr4 using 1)lower 2)in
string =input("enter a string")
c=v=0
string=string.lower()
for s in string:
	if s.isalpha():
		if s in ['a','e','o','i','u']:
			v=v+1
		else:
			c=c+1
	

print("vowels: ",v,"cons",c)