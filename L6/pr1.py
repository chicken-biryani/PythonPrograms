'''wap to find wethwer string are anagram'''

def mysort(s):    	#function definition
	d=sorted(s)
	s=''.join(d)
	return s

s1=input("enter first string")
n1=mysort(s1) #function invocation /calling the function

s2=input("enter second string")
n2=mysort(s2)

if n1==n2:
	print("anagram")
else:
	print("not an anangram")