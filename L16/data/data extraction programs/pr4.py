import socket
import requests
try:
	socket.create_connection( ("www.google.com", 80))
	paper_url=""
	r = requests.get(paper_url)
	with open("Paper.pdf", 'wb') as f:
		f.write(r.content)
except OSError as e:
	print("issue ", e)
