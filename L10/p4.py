import time
import threading
balance = 500
s = threading.Semaphore()
def deposit():
	s.acquire()
	print("Depositing process started ")
	global balance
	amt1 = balance
	amt1 = amt1 + 100
	time.sleep(2)
	balance = amt1
	print("depositing process ended ")
	s.release()
def withdraw():
	s.acquire()
	print("Withdrawl process started ")
	global balance
	amt1 = balance
	amt1 = amt1 - 100
	time.sleep(2)
	balance = amt1
	print("Withrdrawl process ended ")
	s.release()
print("intial balance ",balance)
d1 = threading.Thread(target = deposit)
w1 = threading.Thread(target = withdraw)
d1.start()
w1.start()
d1.join()
w1.join()
print("Final balance ",balance)


















































