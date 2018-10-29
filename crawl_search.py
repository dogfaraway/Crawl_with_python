import requests

kv = {'wd': 'Python'}
r = requests.get('http://www.baidu.com/s', params=kv)
r.status_code
r.request.url
len(r.text)

# baidu
import requests

keyword = 'Python'
try:
    kv = {'wd': keyword}
    r = requests.get('http://www.baidu.com/s', params=kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print('爬取失败')

# 360
import requests

keyword = 'Python'
try:
    kv = {'q': keyword}
    r = requests.get('http://www.so.com/s', params=kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print('爬取失败')
