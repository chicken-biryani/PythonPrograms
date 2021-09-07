'''wapp to read username and password from the user if username is "batman" and password is "ironman"
    then o/p "welcome" else "try again" '''

import getpass
username = input("Enter username ")
password = getpass.getpass("Enter password ")

if( (username == "batman") and (password == "ironman") ):
	print("Welcome")
else:
	print("try again")