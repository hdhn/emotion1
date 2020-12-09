import requests
import bs4
import time

baseUrl = "https://movie.douban.com/top250"


def getUrl(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                      " (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
    }
    req = requests.get(url, headers=head)
    return req.text


# dataList = [getUrl(baseUrl+"?start="+str(x)) for x in range(0,250,25)] #列表生成式直接生成列表代码量少但是占用内存多，数据量大容易溢出
dataListG = (getUrl(baseUrl + "?start=" + str(x)) for x in range(0, 250, 25))  # 生成器保存算法，节省内存空间,只占用一个元素的空间

count = 1
# for i in dataList:
for i in dataListG:
    soup = bs4.BeautifulSoup(i,"html.parser")
    a = soup.findAll('div', class_='info')  # 貌似有歧义class要带下划线
    for j in a:
        print(j.find("span", class_="title").text)
        print(count)
        count += 1
