import socket
import requests
try:
	socket.create_connection( ("www.google.com", 80))
	mn = input("enter movie name ")
	a1 = "http://www.omdbapi.com/?"
	a2 = "&apikey=b88add31"
	a3 = "&s=" + mn
	res = requests.get(a1+a2+a3)
	print(res)
except OSError as e :
	print("check network ", e)
