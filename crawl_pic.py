import requests

path = 'd:/abc.jpg'

url = 'http://image.ngchina.com.cn/2018/1016/20181016044417385.jpg'

r = requests.get(url)

r.status_code

with open(path, 'wb') as f:
    f.write(r.content)

# 全代码

import requests
import os

url = 'http://image.ngchina.com.cn/2018/1016/20181016044417385.jpg'
root = 'd://pics//'
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r= requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print('文件保存成功')
    else:
        print('文件已存在')
except:
    print('爬取失败')