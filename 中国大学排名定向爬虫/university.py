import requests
from bs4 import BeautifulSoup
import bs4
def getHTMLText(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def fillUnivList(ulist,html):
    soup = BeautifulSoup(html,"html.parser")
    #print(soup)
    for tr in soup.find('tbody').children:
        print(tr)
        if isinstance(tr,bs4.element.Tag):
            tds = tr('td')
            #print(tds)
            ulist.append([tds[0].string,tds[1].string,tds[4].string])
    pass

def printUnivList(ulist,num):
    tplt = "{0:^10}\t{1:{3}^12}\t{2:^10}"
    print(tplt.format("排名","学校名称","总分",chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0],u[1],u[2],chr(12288)))

def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2020.html'
    html = getHTMLText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,20)

if __name__ == '__main__':
    main()
    # response = requests.get(url ='https://verify.meituan.com/v2/captcha?request_code=4d82cfcfc5fd469baa2821f139eda4a7&action=spiderindefence&randomId=0.004648075305734967')
    # print(response.text)