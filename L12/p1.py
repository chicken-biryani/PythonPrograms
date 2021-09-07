#wapp to check if ur connected to internet

import socket

try:
	socket.create_connection( ("www.google.com",80) )
	print("u r connected")
except OSError:
	print("Check network")