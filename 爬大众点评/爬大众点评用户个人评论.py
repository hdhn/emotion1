import sys
import os
import re
import requests,csv
from pyquery import PyQuery as pq
import time,random

headers = {
    'Cookie':'_lxsdk_cuid=1753bb608fbc8-0be3842885820b-6b111b7e-1fa400-1753bb608fcc8; _lxsdk=1753bb608fbc8-0be3842885820b-6b111b7e-1fa400-1753bb608fcc8; _hc.v=8429fd3f-f5ca-d6a9-fe0f-58cf71ca55b9.1603024588; s_ViewType=10; ua=%E5%8B%BF%E5%BF%98%E5%BF%83%E5%AE%89_9104; ctu=7fc965fa839279cab50ca6c42a998102e40f1aa3353081dc3b314009932e84da; cy=3; cye=hangzhou; fspop=test; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1604664308,1604725118,1604733097,1604803294; expand=yes; lgtoken=0566ca463-7d8a-4c29-af5c-ea170050929a; dper=3f26651da7054af7dca343e21ad69bdc6f91a7588301e068a064b99e025dd9a782e503b28f14f049b0f4fba030f19d24de83dd48628e97b64b91c174bbac53ccfd4e43b3a9b487476a7e94c21790587361f6279370002dbbcdf6455a7fc3a4b9; ll=7fd06e815b796be3df069dec7836c3df; uamo=13247877023; dplet=6bd483acbc22aa4d4c25fa9c5f38d37c; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1604840844; _lxsdk_s=175a7f72bac-a3-5f1-226%7C%7C173',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36',
    'Referer': 'http://www.dianping.com/shop/G6kUCGwA3SRz95w5/review_all'
}
url = 'http://www.dianping.com/member/1070172'
response = requests.get(url =url,headers = headers)
doc = pq(response.text)
print(doc("span.col-exp"))