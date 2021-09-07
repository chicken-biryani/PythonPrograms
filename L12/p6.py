import bs4
import requests

res = requests.get("https://www.brainyquote.com/quotes_of_the_day.html")
print(res)

soup = bs4.BeautifulSoup(res.text,'lxml')
quote = soup.find('img',{"class":"p-qotd"})
#print(quote)

text = quote['alt']
print(text)
pic = "https://www.brainyquote.com" + quote['data-img-url']
print(pic)
r = requests.get(pic)
import datetime
date = datetime.datetime.now().date()
fn = str(date)+".jpg"
with open(fn, "wb") as f:
	f.write(r.content)