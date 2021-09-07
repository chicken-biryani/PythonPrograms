import socket
try:
	socket.create_connection(("www.google.com",80))
	print("u are connected")
#80 is port number
except OSError as e:
	print("issue",e)