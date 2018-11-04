import requests

r = requests.get('http://python123.io/ws/demo.html')
demo = r.text

from bs4 import BeautifulSoup

soup = BeautifulSoup(demo, 'html.parser')

soup.head
soup.head.contents  # 头部的子节点
soup.body.contents  # body的子节点
soup.body.descendants
len(soup.body.contents)  # body的子节点的数量
soup.body.contents[0]  # 打印第一个body的子节点
soup.body.contents[1]
soup.body.contents[2]
soup.body.contents[3]
soup.body.contents[4]

# 遍历body的子节点
for child in soup.body.contents:
    print(child)
# 遍历body的所有子孙节点
for child in soup.body.children:
    print(child)
# 遍历body的所有子孙节点
soup.body.descendants
for child in soup.body.descendants:
    print(child)

# 父节点
soup = BeautifulSoup(demo, 'html.parser')
soup.title.parent
soup.html.parent
soup.parent

# 上行遍历先辈节点
soup = BeautifulSoup(demo, 'html.parser')
for parent in soup.a.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)

#  前序后序节点
soup = BeautifulSoup(demo, 'html.parser')
print(soup.a.next_sibling)
soup.a.next_sibling.next_sibling
soup.a.previous_sibling
soup.a.previous_sibling.previous_sibling
soup.a.parent

# 标签树的平行遍历
for sibling in soup.a.next_siblings:
    print(sibling)
for sibling in soup.a.previous_siblings:
    print(sibling)

