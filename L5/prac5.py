''' wapp5 to remove the vowels from the string given by the user
i/p:	kamal classes	o/p: kml clsss
i/p:	pinnacle	o/p: pnncl '''

s1 = input("enter a string ").lower()
ns1 = s1

for s in s1:
	if (s=='a'or s=='e' or s=='i' or s=='o' or s=='u'):
		ns1=ns1.replace(s,"")

print("original ", s1, " modified ", ns1)