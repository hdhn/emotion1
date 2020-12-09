from bs4 import BeautifulSoup
import requests
import chardet
url='http://www.edu.cn/'
ua={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}
rq1=requests.get(url,headers=ua)
rq1.encoding=chardet.detect(rq1.content)['encoding']
html=rq1.content.decode('utf-8')
soup=BeautifulSoup(html,'lxml')
print("格式化后BeautifulSoup对象：",soup.prettify())
print('---------------------------------------------------------------')
print("获取head标签：",soup.head)
print(soup.title)
print(soup.body.a)
print("所有的a标签的数量：",len(soup.find_all('a')))

print(soup.name)
print(soup.a.name)
tag=soup.a
print(tag.name)
tag.name='b'
print(tag.name)

print("tag对象的所有属性：",tag.attrs)
print(tag['class'])

tag['class']='css1'
print(tag.attrs)

tag['id']='css2'
del tag['class']
print(tag)

tag=soup.title
print(tag.string)
print(type(tag.string))
tag.string.replace_with('教育科研网')
print(tag.string)

print(type(soup))
print(soup.name)
print(soup.attrs)

mu="<c><!--This is a markup--></b>"
soup_comment=BeautifulSoup(mu,"lxml")
print(soup_comment.c.string)
print(type(soup_comment.c.string))
print('------------------------------------------------------------')

print("标签名为title的全部节点：",soup.find_all('title'))
print(soup.title.string)
print(soup.title.get_text())

tag1=soup.ul.find_all('a')
print(tag1)
url1=[]
txt1=[]
for t1 in tag1:
    url1.append(t1.get('href'))
    txt1.append(t1.get_text())
for i in url1:
    print(i)
for j in txt1:
    print(j)