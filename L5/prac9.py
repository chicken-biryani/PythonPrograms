'''wap to check wether anagram. two word havving same letters'''

s1 = input("enter string 1 ")
s2 = input("enter string 2 ")

a=sorted(s1)
b=sorted(s2)

if a==b:
	print("anagram")
else:
	print("nahi")




