import requests

r = requests.get('http://python123.io/ws/demo.html')
demo = r.text

from bs4 import BeautifulSoup

soup = BeautifulSoup(demo, 'html.parser')
for link in soup.find_all('a'):
    print(link.get('href'))

soup.find_all('a')
soup.find_all(['a', 'b'])

for tag in soup.find_all(True):
    print(tag.name)

import re

for tag in soup.find_all(re.compile('b')):
    print(tag.name)

soup.find_all('p', 'course')
soup.find_all(id='link1')
soup.find_all(id='link')
# 引入正则表达式
import re

soup.find_all(id=re.compile('link'))

soup.find_all('a')
soup.find_all('a',recursive=False)

soup.find_all(string = 'Basic Python')
import re
soup.find_all(string = re.compile('Python'))
