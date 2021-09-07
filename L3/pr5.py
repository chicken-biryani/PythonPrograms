# password and username
import getpass
s1= input("enter a Username ")

s2= getpass.getpass("enter a password ")

if(s1=="kamal" and s2=="classes"):  
	print("welcome")
else:
	print("nbye")

