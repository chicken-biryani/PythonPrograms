''' wapp4 to count the number of vowels (a,e,i,o,u) and consonants in the
string given by the user '''


s1 = input("enter a string ").lower()
vc, cc = 0, 0

for s in s1:
	if (s.isalpha()):
		if (s=='a' or s=='e' or s=='i' or s=='o' or s=='u'):
			vc = vc + 1
#u could also type s in ['a','e','i','o','u']
		else:
			cc = cc + 1
print("vowel count = ", vc, " consonant count = ", cc)

