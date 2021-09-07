''' wapp3 to count the number of lowercase letters and number of
uppercase letters	'''

s1 = input("enter a string ")
lc, uc = 0, 0

for s in s1:
	if (s.isalpha()):
		if(s.islower()): 
			lc = lc + 1
		else:
			uc = uc + 1
print("lower case count ", lc, " upper case count ", uc)