#wapp to check if the string is palindrome or not

s1=input("Enter a string ")
s1 = s1.lower() #use this if u want case in sensitive comp
r1=s1[::-1]
if s1 == r1:
	print("Palindrome")
else:
	print("Not Palindrome") 