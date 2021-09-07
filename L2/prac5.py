#Wapp to read marks and find grade
#	m>=70  G=Dist
#	m>=60  G=FC
#	m>=50  G=SC
#	m>=40  G=PC
#	else       G=Fail

m=int(input("Enter marks "))
G=' '

if m>=70:
	G="Dist"

elif m>=60:
	G='FC'

elif m>=50:
	G='SC'

elif m>=40:
	G='PC'

else:
	G='Fail'

print("Marks = ",m, "Grade = ",G)