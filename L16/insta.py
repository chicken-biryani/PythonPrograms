import socket
import requests

try:
	socket.create_connection(("www.google.com",80))
	print("u are connected")
	res=requests.get("https://www.instagram.com/direct/t/340282366841710300949128379267731365213")
	print(res)  #usually koi number aatay .. 200 ig
	data=res.json()   #dict{key:value}
	print(data)
	#ip = data['ip']   #dictionary with key ip
	#print("ip address",ip)
	#city_name=data['city']
	#print("city ",city_name)
except OSError as e: 
	print("issue",e)

	