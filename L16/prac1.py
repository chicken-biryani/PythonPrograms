"""this program uses concepts of beautiful scoop(web scraping),socket and requests.It gives the quote of the day
from a site called "brainy quotes".. its a dynamic program as the quote on the page changes everyday"""
import socket
import requests
import bs4 
try:
	name = input("Hello there ... please enter your name ")
	print("Hello ",name)
	socket.create_connection(("www.google.com",80))
	print("u are connected")
	
	res=requests.get("https://www.brainyquote.com/quote_of_the_day")
	#print(res)
	soup = bs4.BeautifulSoup(res.text,'lxml')
	data=soup.find("img",{"p-qotd"})
	#print(data)
	motd=data['alt']
	print("quote of the day is")
	print(motd)
	
except Exception as e:
	print("issue")