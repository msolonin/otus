import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.google.com")

# https://www.crummy.com/software/BeautifulSoup/bs4/doc.ru/bs4ru.html
page = BeautifulSoup(req.text)
print(page.title)
print(page.title.name)
print(page.title.string)
print(page.title.parent.name)
print(page.find_all('a'))
print(page.find(id="hplogo"))
print(page.prettify())
