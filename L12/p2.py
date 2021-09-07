#wapp to get the latitude and longitude

import socket
import requests
try:
	socket.create_connection( ("www.google.com",80) )
	res = requests.get("https://ipinfo.io/")
#	print(res)
	data = res.json()
#	print(data)
	city = data['city']
	print(city)
	loc = data['loc']
	print(loc)
	info = loc.split(",")
	lat = info[0]
	lon = info[1]
	print("Latitude = ",lat)
	print("Longitude = ",lon)
except OSError:
	print("check network")