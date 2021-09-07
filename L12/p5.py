import requests
mn = input("Enter movie name ")
a1 = "http://www.omdbapi.com/?"
a2 = "&apikey=b88add31"
a3 = "&s=" + mn
res = requests.get(a1+a2+a3)
#print(res)
data = res.json()
print(data)
search = data['Search']
for s in search:
	title = s['Title']
	year = s['Year']
	poster = s['Poster']
	print("Title = ",title,"Year = ",year)
	if poster != "N/A":
		r = requests.get(poster)
		fn = str(title)+".jpg"
		with open(fn, "wb") as f:
			f.write(r.content)