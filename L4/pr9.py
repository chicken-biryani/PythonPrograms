#anagram
s=input("enter a string 1 ")
data= sorted(s) #returns a list
a=input("enter a string 2 ")
data2= sorted(a) 
d=''.join(data)
e=''.join(data2)

if d==e:
	print("anagram")
else:
	print("nope")
