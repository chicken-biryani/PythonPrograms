#wapp to read two range from user r1 and r2 inclusive
#if num is multple of 3 -- amar 5-- albar 3&5-- anthony


r1=int(input("enter lower range"))
r2=int(input("enter up range"))
if r1 > r2:
 r1, r2= r2,r1

for i in range(r1, r2+1):
	if i%3==0 and i%5==0:
		print(i,"anthony")
	elif i%3==0: 
		print(i,"amar")
	elif i%5==0:
		print(i,"akbar")