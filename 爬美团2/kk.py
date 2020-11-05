import requests
from bs4 import BeautifulSoup
from lxml import etree
import json

url = 'https://bj.meituan.com'
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'uuid=c5912c800e394ef59009.1590753374.1.0.0; ci=1; rvct=1; _lxsdk_cuid=172604a352b62-02b87e29c1eeb2-1b386257-13c680-172604a352cc8; __mta=44275227.1590753376341.1590753376341.1590753376341.1; _lxsdk_s=172604a352e-c7a-467-f4f%7C%7C2',
    'Host': 'bj.meituan.com',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
}


def get_start_links(url):
    html = requests.get(url).text
    tree = etree.HTML(html)
    node = tree.xpath("//div[@class='b-n-sublist']")
    # print(node)

    ii = node[1].xpath("dd[@class='b-n-list-item']/a/@href")
    # exit()
    # print(html)
    # soup = BeautifulSoup(html,'lxml')
    # links = [link.find('ul').find('li').find('span').find('span').find('a')['href'] for link in soup.findAll(name='div',class_='category-nav-content-wrapper')]
    # links =soup.findAll(name='a',attrs={"href":re.compile(r'^http:')})
    print(ii)
    # for link in links:
    #     print(link.get('href'))
    return ii
def get_store(url):
    html = requests.get(url).text
    tree = etree.HTML(html)
    # print(html)
    # exit()
    # node = tree.xpath("")
    # return node

def get_detail_id(url,headers=None):
    html= requests.get(url,headers=headers).text
    soup= BeautifulSoup(html,'lxml')
    context_id = json.loads(soup.find())

start_url_list = get_start_links(url)
for url in start_url_list:
    start_store = get_store(start_url_list[1])
