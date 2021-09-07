import socket
import requests

try:
	socket.create_connection(("www.google.com",80))
	print("u are connected")
	res=requests.get("https://ipinfo.io/")
	print(res)  #usually koi number aatay .. 200 ig
	data=res.json()   #dict{key:value}
	print(data)
	ip = data['ip']   #dictionary with key ip
	print("ip address",ip)
	city_name=data['city']
	print("city ",city_name)
except OSError as e: 
	print("issue",e)

	