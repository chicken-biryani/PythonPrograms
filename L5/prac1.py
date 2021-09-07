"""wap to see word is palidrome eg:nitin,mam,racecar"""

s1=input("enter the word ").lower()
r1=s1[::-1]

if s1 == r1:
	print("yes")
else:
	print("no")



