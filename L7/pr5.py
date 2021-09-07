marks =[]

r=input("would you like to add more marks ")

while(r=='y'):
	marks.append(int(input("enter ")))
	r=input("would u like to add more marks")

marks.sort()

print(marks[len(marks)-1]) #sir ke ismein marks[-1] hua
print(marks[0])