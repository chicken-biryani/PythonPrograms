#wapp tp check if the given two strings are anagrams using function
#i/p: s1-listen  s2-silent 

def mysort(s):
	s=sorted(s)
	s= ''.join(s)
	return s

s1 = input("Enter 1st String ")
s1 = mysort(s1)

s2 = input("Enter 2nd String ")
s2 = mysort(s2)

if s1 == s2:
	print("Anagram")
else:
	print("Not Anagram")
