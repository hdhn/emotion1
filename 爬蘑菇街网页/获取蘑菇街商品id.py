import requests,time,csv,random
import json
import re
from bs4 import BeautifulSoup

headers = {
    # 'accept': '*/*',
    # 'accept-encoding': 'gzip, deflate, br',
    # 'accept-language': 'zh-CN,zh;q=0.9',
    'cookie':'__mgjuuid=f1672d9a-25bc-4835-85d0-1a39654cb591; _mwp_h5_token_enc=874d4b90cbe24b1d48addf9cc3ed5569; _mwp_h5_token=2d9638e2560470ec7edaddd2dcfcca21_1601259970436; _ga=GA1.2.919819752.1601260014; _gid=GA1.2.663241931.1601260014; __mgjref=https%3A%2F%2Fwebim.mogu.com%2Fh5%3Fptp%3D32._mf1_1239_70922.0.0.FsupgHDL%26acm%3D3.mf.1_0_0.0.0.0.mf_70922_1043091; mf_cache=xNK728q1RCOo03XT7kkXRg; FRMS_FINGERPRINTN=xNK728q1RCOo03XT7kkXRg; JSESSIONID=D2BD990D7323A237FB5FCCA4D925EE9D; _gat=1',
    'referer': 'https://shop.mogu.com/detail/1msv64s?acm=3.ms.1_4_1msv64s.15.1343-102817-68998.jMfkbsc4JCHJ0.sd_117-swt_15-imt_6-c_1_3_573111237_0_0_3-t_jMfkbsc4JCHJ0-lc_3-fcid_50240-pid_180-pit_1-dit_-idx_0-dm1_5002&cparam=MTYwMTQ3MDE2OV8xMWtfY2JlZDE2MjQ5YzA3OGY4ZmJhNGZmMjdjZjE2ZGQ5MDJfM18wXzU3MzExMTIzN180NV8wXzBfMF83MzZfMV8zX2xvYy0w&ptp=31.Onv5v.0.0.3BF16jEF',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3775.400 QQBrowser/10.6.4209.400'
}
url ='https://list.mogu.com/search?callback=_version=8193&ratio=3%3A4&cKey=15&page={page}&sort=pop&ad=0&fcid=&action=clothing&ptp=31.vOv15b.0.0.9IN4ueBW&'


def get_mogu_ItemId(url):
    response = requests.get(url=url, headers=headers)
    htmls = response.json()['result']['wall']['docs']
    fp = open("./蘑菇街商品id1.csv",'a',newline = '',encoding='utf-8-sig')
    writer = csv.writer(fp)#我要写入
    for html in htmls:
        writer.writerow((html['title'],html['tradeItemId']))
        print(html['tradeItemId'])
    fp.close()
for i in range(1, 50):
    try:
        url1 = url.format(page = i)
        get_mogu_ItemId(url1)
        time.sleep(random.randint(1, 3))
    except:
        print("爬取完成")
        break

