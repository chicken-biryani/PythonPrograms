import socket
import requests
try:
	socket.create_connection( ("www.google.com", 80))
	res = requests.get("https://ipinfo.io/")
	print(res)
	data = res.json()
	print(data)
	ip=data['ip']
	print(" ip address is ",ip)
	city=data['city']
	print("city name is ",city)
	location=data['loc']
	a=location.split(",")
	print(a[0])
	print(a[1])
except OSError as e:
	print("issue ", e)
