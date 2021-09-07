#to read two integers and exchange them
#i. using 3rd variable
#2.without using 3rd variable


n1 = int(input("Enter 1st number "))

n2 = int(input("Enter 2nd number "))
print("n1= ",n1)
print("n2= ",n2)

n1,n2 = n2,n1

print("n1= ",n1, "n2= ",n2)