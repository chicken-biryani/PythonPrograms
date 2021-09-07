from datetime import *

dt= datetime.now()
hour=dt.hour
msg=""
if(hour>6 and hour<12):
	msg="GM"
elif(hour>=12 and hour<6):
ea	msg="GA"
else:
	msg="GE"

print(msg," ",dt)
