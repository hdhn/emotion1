import sys
import os
import re
import requests,csv
from pyquery import PyQuery as pq
import time,random

headers = {
    'Cookie':'cy=3; cye=hangzhou; _lxsdk_cuid=1753f165f9ec8-0cb558ba6b0e3a-6b111b7e-144000-1753f165f9fbe; _lxsdk=1753f165f9ec8-0cb558ba6b0e3a-6b111b7e-144000-1753f165f9fbe; _hc.v=9030c7fe-0b57-e105-ffa5-45d14dae3ce0.1603081232; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1603081232,1603081243; ll=7fd06e815b796be3df069dec7836c3df; ua=%E5%8B%BF%E5%BF%98%E5%BF%83%E5%AE%89_9104; ctu=7fc965fa839279cab50ca6c42a9981023b8d10bde71e72095032b366399a6fe8; uamo=13247877023; s_ViewType=10; lgtoken=0dbdbb3d7-2b1b-44f1-8ba0-e3c6f2ae19c4; dper=6ca497a6a0c26059a5a364a6b070325ec1076c43c7005b7f1b8ba9e503cd1cb5159bbdd3f3e434a0a021e7cbb082aa7288a6bf778a07a425cf22b4582d2e5429dc3000e72f93ab2dc14bac6d108649ded077f28916d019ac53718c7e7ed00545; dplet=2ebc7cdaeb581c6d34f6c594245e64d5; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1605011321; _lxsdk_s=175b21febc2-eb7-650-dc4%7C%7C18',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36',
    'Referer': 'http://www.dianping.com/member/45119307'
}
url = 'http://www.dianping.com/member/45119307'
response = requests.get(url =url,headers = headers)
doc = pq(response.text)
#print(doc)
zhuce_shijian = doc("div.user-time>p").text()[-15:]
print(zhuce_shijian)
url1 = url+'/reviews'
response1 = requests.get(url = url1,headers = headers)
doc1 = pq(response1.text)
pinglun_didian =doc1('h6').items()
for item in pinglun_didian:
    print(item.text())
print(pinglun_didian)
pinglun_shijian = doc1('span.col-exp').items()
for item in pinglun_shijian:
    print(item.text())
print(pinglun_shijian)



