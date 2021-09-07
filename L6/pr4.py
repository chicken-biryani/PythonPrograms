''' wapp4 to read a sentence and 
create new sentence in which every word is reversed
i/p: 	kamal classes thane
o/p:    lamak sessalc enaht
'''

def rev_string(s):
	a=s[::-1]
	return a

s1 = input("enter a sentence ")
d1 = s1.split(' ')
ns1 = ""

for d in d1:
	ns1 =ns1+' '+rev_string(d)

print("original ", s1, " modified ", ns1)


   