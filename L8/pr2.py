word=input("enter a sentence ")

dict={}
a=word.split(' ')
for c in a:
	co = dict.get(c,0)
	if co == 0:
		dict[c]=1
	else:
		dict[c]=co+1
print(dict)		
