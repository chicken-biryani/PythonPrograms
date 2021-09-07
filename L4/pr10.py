
#anagream using functions

def mysort(a):
	data= sorted(a) 
	b=''.join(data)
	return b
s1=input("enter a string 1 ")
d=mysort(s1)
s2=input("enter a string 2 ")
e=mysort(s2)


if d==e:
	print("anagram")
else:
	print("nope")
