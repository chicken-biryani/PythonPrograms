#wapp to get the temp of : Mumbai,Singapore and Dubai

import socket
import requests
try:
	cities = ['mumbai','singapore','dubai']
	for city in cities:
		socket.create_connection( ("www.google.com",80) )
		a1 = "http://api.openweathermap.org/data/2.5/weather?units=metric"
		a2 = "&q=" + city
		a3 = "&appid=c6e315d09197cec231495138183954bd"
		api_address = a1 + a2 + a3
		res1 = requests.get(api_address)
		data = res1.json()
		main = data['main']
		temp = main['temp']
		print("city = ",city , "temp = ", temp)
except OSError:
	print("check network")