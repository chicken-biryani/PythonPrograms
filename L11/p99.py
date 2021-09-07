import p5

try:
	day=int(input("enter the day "))
	month=int(input("enter the month "))
	year=int(input("enter the year "))
	p5.age(day,month,year)
except TypeError:
	print("enter the value of day/month/year in the form of integer")
except:
	print("issue")