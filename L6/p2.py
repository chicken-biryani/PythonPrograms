'''wapp to read two set of names : 1) java students  2)android students
	find	1)total names	2)common names
		3)students in java but not android '''

java = set()
android = set()

ans = input("Do you want to add java student y/n ")
while ans == 'y':
	n = input("Enter name ")	
	java.add(n)
	ans = input("Do you want to add more java student y/n ")


ans = input("Do you want to add android student y/n ")
while ans == 'y':
	n = input("Enter name ")	
	android.add(n)
	ans = input("Do you want to add more android student y/n ")

total=java | android
print("Total Students ",total)

common=java & android
print("Common Students ",common)

diff = java - android
print("In java but not android ",diff)







