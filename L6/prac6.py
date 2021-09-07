

java=set()
android=set()

reply = input("do enters names of java y/n")
while reply == 'y':
	name= (input("enter name "))
	java.add(name)
	reply = input("do u want to add some more names y/n  ")

reply = input("do enters names of android batch y/n")
while reply == 'y':
	name= (input("enter name "))
	android.add(name)
	reply = input("do u want to add some more names y/n  ")

print("in all",java|android)
print("in both",java&android)
print("in java not android",java-android)