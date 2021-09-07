#wapp tp check if the given two strings are anagrams 
#i/p: s1-listen  s2-silent 

s1 = input("Enter 1st String ")
s1=sorted(s1)
s1= ''.join(s1)
	
s2 = input("Enter 2nd String ")
s2=sorted(s2)
s2= ''.join(s2)

if s1 == s2:
	print("Anagram")
else:
	print("Not Anagram")
