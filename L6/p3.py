#wapp tp read a string and count tjhe occurrence of each letter
#i/p:kamal  o/p: k-1,a-2,m-1,l-1

count = { }
str = input("Enter a String ")
for s in str :
	c = count.get(s,-1)
	if c == -1:
		count[s] = 1
	else:
		count[s] = c + 1

print(count)
   