'''wap to read list of integers and print em'''

marks =[]

r=input("would you like to add more marks ")

while(r=='y'):
	marks.append(int(input("enter ")))
	r=input("would u like to add more marks")
sum=0
for i in range(0,len(marks)):
	sum = marks[i]+sum

print(sum)
print(sum/len(marks))