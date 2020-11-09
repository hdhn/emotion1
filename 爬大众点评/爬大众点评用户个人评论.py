import sys
import os
import re
import requests,csv
from pyquery import PyQuery as pq
import time,random

headers = {
    'Cookie':'cy=3; cye=hangzhou; _lxsdk_cuid=1753f165f9ec8-0cb558ba6b0e3a-6b111b7e-144000-1753f165f9fbe; _lxsdk=1753f165f9ec8-0cb558ba6b0e3a-6b111b7e-144000-1753f165f9fbe; _hc.v=9030c7fe-0b57-e105-ffa5-45d14dae3ce0.1603081232; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1603081232,1603081243; ll=7fd06e815b796be3df069dec7836c3df; ua=%E5%8B%BF%E5%BF%98%E5%BF%83%E5%AE%89_9104; ctu=7fc965fa839279cab50ca6c42a9981023b8d10bde71e72095032b366399a6fe8; uamo=13247877023; s_ViewType=10; dper=d86a3b49d91f937c7cbd1d87b60198b76c64fbcb54dbefe112fa66b4cc70916b8dd38409e81fec8f3e2ee020a2ef8bba608a90c569eadcf00f111cdccaa06f0632e689fe069cbc47f95c04946e96ae7849a229ce834e9658328e8517b59cf3fb; dplet=94f0e8aba09e0a24aa4b8eee32f36b73; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1604910187; _lxsdk_s=175ac1797a3-5e-261-c47%7C%7C318',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36',
    'Referer': 'http://www.dianping.com/shop/G6kUCGwA3SRz95w5/review_all'
}
url = 'http://www.dianping.com/member/2013016606'
response = requests.get(url =url,headers = headers)
doc = pq(response.text)
#print(doc)
zhuce_shijian = doc("div.user-time>p").text()[-15:]
print(zhuce_shijian)
url1 = url+'/reviews'
response1 = requests.get(url = url1,headers = headers)
doc1 = pq(response1.text)
pinglun_shijian =doc1('h6')
print(pinglun_shijian)


