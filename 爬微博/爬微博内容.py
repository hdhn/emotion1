import requests
from bs4 import BeautifulSoup
import csv
headers = {

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3775.400 QQBrowser/10.6.4209.400'
}

url = 'https://s.weibo.com/weibo?q=%E7%9B%B4%E6%92%AD%E9%80%80%E8%B4%A7&wvr=6&b=1&Refer=SWeibo_box#_loginLayer_1602233075684'
response = requests.get(url = url,headers = headers)
print(response)
soup = BeautifulSoup(response.text,'lxml')
htmls =soup.find_all('p',class_="txt")
# for html in htmls:
#     for i in html.find_all('em'):
#         print(i.contents)

# print(htmls)
fp = open("./微博搜索内容.csv", 'a', newline='', encoding='utf-8-sig')
writer = csv.writer(fp)  # 我要写入

for html in htmls:
    nick_name = html.get('nick-name')
    writer.writerow(("用户名称",nick_name))
    #content = re.compile(r'<.*?>')
    content = html.contents
    writer.writerow(("微博内容",content))
fp.close()