import requests

r = requests.get('http://python123.io/ws/demo.html')
demo = r.text

from bs4 import BeautifulSoup
soup = BeautifulSoup(demo,'html.parser')
soup.prettify()
print(soup.prettify())
print(soup.a.prettify())

soup = BeautifulSoup('<p>中文</p>','html.parser')
soup.p.string
print(soup.p.prettify())