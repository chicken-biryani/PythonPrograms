'''
wapp
1.to connect openweathermap.org got temp = "Mumbai","Singapore","Dubai" 
2. to plot temp as bar:
'''
import socket
import requests
import matplotlib.pyplot as plt

cities = ['mumbai','singapore','dubai']
temperature = []
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
	temperature.append(temp)
plt.bar(cities, temperature)
plt.title("Weather Report")
plt.xlabel("Cities")
plt.ylabel("Temperature")
plt.savefig("weather.png")
plt.show()



