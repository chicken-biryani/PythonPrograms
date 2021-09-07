#Wapp to read year from user & find if it is a leap year

yr = int(input("Enter yr "))

#check every 4 years
b1 = (yr%100 != 0) and (yr%4 == 0) 	

#check every 400 years 
b2 = (yr%100 == 0) and (yr%400 == 0)	
if b1 or b2:
	print("LEAP YEAR")
else:
	print("not LEAP YEAR")
