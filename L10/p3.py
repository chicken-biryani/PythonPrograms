import time
import threading
balance = 500
def deposit():
	print("Depositing process started ")
	global balance
	amt1 = balance
	amt1 = amt1 + 100
	time.sleep(2)
	balance = amt1
	print("depositing process ended ")
def withdraw():
	print("Withdrawl process started ")
	global balance
	amt1 = balance
	amt1 = amt1 - 100
	time.sleep(2)
	balance = amt1
	print("Withrdrawl process ended ")

print("intial balance ",balance)
d1 = threading.Thread(target = deposit)
w1 = threading.Thread(target = withdraw)
d1.start()
w1.start()
d1.join()
w1.join()
print("Final balance ",balance)





