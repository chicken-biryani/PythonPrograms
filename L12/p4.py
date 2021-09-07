import requests

paper_url = "http://old.mu.ac.in/wp-content/uploads/2014/11/1T01226.pdf"

res = requests.get(paper_url)
print(res)

with open("paper.pdf", "wb") as f:
	f.write(res.content)
	print("download complete")