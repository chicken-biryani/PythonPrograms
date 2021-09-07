import threading
import time
def write():
	print("writing started ")
	for i in range(1, 6):
		print("writing ", i , " assignment " )
		time.sleep(2)
	print("writing completed ")
def music():
	print("music started ")
	for i in range(1, 21):
		print("playing ", i , " song " )
		time.sleep(1)
	print("music completed ")
print("aaj ka kaam shuru ")
w1 = threading.Thread(target=write)
m1 = threading.Thread(target=music)
w1.start()
m1.start()
w1.join()
m1.join()
print("aaj ka kaam khatam ")
