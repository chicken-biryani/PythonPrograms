#wap to read names as tuple 

names=[]
even_names=[]
odd_names=[]
reply = input("do u want to enters names  y/n")
while reply == 'y':
	name= (input("enter name "))
	names.append(name)
	reply = input("do u want to add some more names y/n  ")


for d in names:
	if(len(d)%2==0):
		even_names.append(d)	
	else:
		odd_names.append(d)

even_data=tuple(even_names)
print("even  ",even_data)
odd_data=tuple(odd_names)

print("odd  ",odd_data)