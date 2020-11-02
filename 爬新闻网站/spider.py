import requests,time,csv
from bs4 import BeautifulSoup
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3754.400 QQBrowser/10.5.4020.400'
}
url = 'http://www.cup.edu.cn/sba/xyxw/index.htm'
response = requests.get(url=url,headers=headers)
text = response.content
soup = BeautifulSoup(text,'lxml')
#dicto= re.findall('<a href="(.*?)">(.*?)</a>',response)
#print(soup.a.attrs['href'])
links = soup.findAll(name='ul',class_='list01')
lins1 = links[0].findAll(name = 'li')
for link in lins1:
    dicto1 = link.a.attrs['href']
    time1 = link.span.text
    title = link.a.text
    #print(time1)
    print(title)
    fp = open("./中石油管理学院新闻.csv", 'a', newline='', encoding='utf-8-sig')
    writer = csv.writer(fp)  # 我要写入
    # 写入内容
    writer.writerow(("标题",title,"时间",time1))  # 运行一次
    url1 = 'http://www.cup.edu.cn/sba/xyxw/{dicto1}'.format(dicto1 = dicto1)
    response = requests.get(url=url1, headers=headers)
    text = response.content
    soup = BeautifulSoup(text, 'lxml')
    links1 = soup.findAll(name='p')
    time.sleep(2)
    for i in range(0,len(links1)):
        writer.writerow(("内容",links1[i].text))
    fp.close()

for page in range(1,11):
    url = 'http://www.cup.edu.cn/sba/xyxw/index{n}.htm'.format(n = page)
    response = requests.get(url=url,headers=headers)
    text = response.content
    soup = BeautifulSoup(text,'lxml')
    #dicto= re.findall('<a href="(.*?)">(.*?)</a>',response)
    #print(soup.a.attrs['href'])
    links = soup.findAll(name='ul',class_='list01')
    lins1 = links[0].findAll(name = 'li')
    for link in lins1:
        dicto1 = link.a.attrs['href']
        time1 = link.span.text
        title = link.a.text
        #print(time1)
        print(title)
        fp = open("./中石油管理学院新闻.csv", 'a', newline='', encoding='utf-8-sig')
        writer = csv.writer(fp)  # 我要写入
        # 写入内容
        writer.writerow(("标题",title,"时间",time1))  # 运行一次
        url1 = 'http://www.cup.edu.cn/sba/xyxw/{dicto1}'.format(dicto1 = dicto1)
        response = requests.get(url=url1, headers=headers)
        text = response.content
        soup = BeautifulSoup(text, 'lxml')
        links1 = soup.findAll(name='p')
        time.sleep(2)
        for i in range(0,len(links1)):
            writer.writerow(("内容",links1[i].text))
        fp.close()