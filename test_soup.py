# test for beautiful soup
import requests

r = requests.get('http://python123.io/ws/demo.html')
demo = r.text

from bs4 import BeautifulSoup

soup = BeautifulSoup(demo, 'html.parser')
print(soup.prettify())

#
from bs4 import BeautifulSoup

soup = BeautifulSoup(demo, 'html.parser')
soup.title
tag = soup.a
tag

#
from bs4 import BeautifulSoup
soup= BeautifulSoup(demo, 'html.parser')
soup.a.name
soup.a.parent.name
soup.a.parent.parent.name

tag = soup.a
tag.attrs

tag.attrs['class']
tag.attrs['href']
type(tag.attrs)
type(tag)

soup.a
soup.a.string
soup.p
soup.p.string
type(soup.p.string)

#
newsoup = BeautifulSoup('<b><!--This is a comment--></b><p>This is not a comment</p>','html.parser')
newsoup.b.string
type(newsoup.b.string)
newsoup.p.string
type(newsoup.p.string)