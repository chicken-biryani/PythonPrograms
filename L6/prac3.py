#wap to read namesa nd findlongsest

names=[]
reply = input("do u want to enters names  y/n")
while reply == 'y':
	name= (input("enter mrks "))
	names.append(name)
	reply = input("do u want to add some more names y/n  ")

print(names)

max=names[0]
for d in names:
	if(len(d)>len(max)):
		max=d

print(max)
		
	