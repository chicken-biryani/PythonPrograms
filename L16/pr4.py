import socket 
import requests
try:
	socket.create_connection(("www.google.com",80))
	paper_url="http://www.mum.digitaluniversity.ac/WebFiles/1S00166n.pdf"
	res=requests.get(paper_url)
	print(res)
	
	f1=None
	try:
		f1=open("p1.pdf","wb")
		f1.write(res.content)
		print("done")
	except Exception as e:
		print("writing issue ",e)
	finally:
		if f1 is not None:
			f1.close()
#second way to do it
	try:
		with open("p2.pdf","wb") as f2:
			f2.write(res.content)
		print("done")
	except Exception as e:
		print("writing issue ",e)

except OSError as e:
	print("issue ",e)
	