import socket
import requests
try:
	socket.create_connection( ("www.google.com", 80))
	res = requests.get("https://ipinfo.io/")
	print(res)
except OSError as e:
	print("issue ", e)