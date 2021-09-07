import socket
import requests
import bs4
try:
	socket.create_connection(("www.google.com",80))
	#print("u are connected")
	
	res = requests.get("https://www.brainyquote.com/quot_of_the_day")
	soup=bs4.BeautifulSoup(res.text,"lxml")

	data = soup.find("img",{"class":"p-qotd"})
	print(data)
	motd=data['alt']
	print(motd)

except Exception as e:
	print("issue",e)
	
	
	soup = bs4.BeautifulSoup(res)