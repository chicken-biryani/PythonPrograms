#wap to count the num of vowels and consonants

string =input("enter a string")
c=v=0
for s in string:
	if s.isalpha():
		if(s =='a' or s =='e' or s =='i' or s=='o' or s=='u'):
			v=v+1
		else:
			c=c+1
	

print("vowels: ",v,"cons",c)