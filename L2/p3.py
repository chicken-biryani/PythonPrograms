#wapp to read if date of month from user 
#if dau=y is even the message "parking on right"
#if day is odd then msg " parking on left"

day=int(input("enter day on month"))

if(day>31 or day<1):
	print("invalid date")
else:
	if (day%2)==0:
		print("park on right side")
	else:
		print("park on the left")