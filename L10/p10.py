#wapp wish the user GM/GA/GE

import datetime
dt = datetime.datetime.now()
hour = dt.hour
msg = ""
if(hour >= 6 and hour < 12):
	msg="Good Morning"
elif(hour >= 1 and hour < 18):
	msg = "Good Afternoon"
else:
	msg = "Good Evening"
print(msg)
