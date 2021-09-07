#wapp to read a string and count the occurrence of each word
#i/p: kamal is kamal sir o/p:

count = { }
str = input("Enter a Sentence ")
lstr = str.split(" ")
for s in lstr :
	c = count.get(s,-1)
	if c == -1:
		count[s] = 1
	else:
		count[s] = c + 1

print(count)