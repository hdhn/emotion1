import requests
from bs4 import BeautifulSoup
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3775.400 QQBrowser/10.6.4208.400',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,zh;q=0.9',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Cookie': '__cfduid=dfa5565117068ac6c68554d5de329cd1b1599140850',
'Host': 'py4e-data.dr-chuck.net',
'Upgrade-Insecure-Requests':'1'
}
n=7
url ='http://py4e-data.dr-chuck.net/known_by_Katelin.html'
while n>0:
    response = requests.get(url,headers =headers)
    soup = BeautifulSoup(response.text,'html.parser')
    htmls = soup.findAll('li')
    print(htmls)
    h=[]
    names = []
    for html in htmls:
        h.append(html.findAll('a')[0].get('href',None))
        names.append(html.a.contents)
    url=str(h[17])
    k=names[17]
    names.clear()
    print(url)
    h.clear()
    n=n-1
print(k)
