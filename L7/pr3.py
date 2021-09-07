'''wap to read list of integers and print em'''

data=[]

r=input("would you like to add integers")

while(r=='y'):
	data.append(int(input("enter ")))
	r=input("would u like to add more integers")
print(data)