from datetime import *
'''to find age'''
try:
	day=int(input("enter day "))
	month=int(input("enter month "))
	year=int(input("enter year "))

	dob=date(year,month,day)
	print(dob)

	today=datetime.now().date()
	age=(today-dob)/timedelta(days=365.24)
	print(round(age,2))
except ValueError as e:
	print("dob issue ",e)

