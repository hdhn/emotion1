import sys
import os
import re
import requests,csv
from pyquery import PyQuery as pq
import time,random

headers = {
    'Cookie':'_lxsdk_cuid=1753bb608fbc8-0be3842885820b-6b111b7e-1fa400-1753bb608fcc8; _lxsdk=1753bb608fbc8-0be3842885820b-6b111b7e-1fa400-1753bb608fcc8; _hc.v=8429fd3f-f5ca-d6a9-fe0f-58cf71ca55b9.1603024588; s_ViewType=10; ua=%E5%8B%BF%E5%BF%98%E5%BF%83%E5%AE%89_9104; ctu=7fc965fa839279cab50ca6c42a998102e40f1aa3353081dc3b314009932e84da; cy=3; cye=hangzhou; fspop=test; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1605786702,1605928795,1606009699,1606009855; expand=yes; lgtoken=095c428b7-cdfa-4d22-93af-a117399501b7; dper=9b19a1a593ad927bca495d81ed4a4786ed1d43d3ee000ad207e8d953de7267954dc40f2c58c9808b95409fce2a928087454caa2737befc4a7862a94599c4144243e0d541c1080a27b436a5063c3473778d8e32e1b2eb8ce5973c0031c1df015f; ll=7fd06e815b796be3df069dec7836c3df; uamo=13247877023; dplet=eb2211390b35b5efb78bc26ab6b88360; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1606009894; _lx_utm=utm_source%3Dwww.sogou%26utm_medium%3Dorganic; _lxsdk_s=175eda33571-854-a69-e0%7C%7C88',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36',
    'Referer': '{url}/reviews'
}
#url = 'http://www.dianping.com/member/8540198'
def get_html(url):
    response = requests.get(url =url,headers = headers)
    doc = pq(response.text)
    #print(doc)
    zhuce_shijian = doc("div.user-time>p").text()[-10:]
    try:
        print(doc("div.user-info>span").attr('class').split(' ')[1].replace('urr-rank',''))
    except:
        input("按enter键继续")
        response = requests.get(url =url,headers = headers)
        doc = pq(response.text)
    user_star = doc("div.user-info>span").attr('class').split(' ')[1].replace('urr-rank','')
    print(user_star)
    print(zhuce_shijian)
    url1 = url+'/reviews'
    headers['Referer'] = headers['Referer'].format(url = url )
    response1 = requests.get(url = url1,headers = headers)
    doc1 = pq(response1.text)
    pinglun_didian =doc1('h6').items()
    pinglun_shijian = doc1('span.col-exp').items()
    pinglunds={}
    for item1,item2 in zip(pinglun_didian,pinglun_shijian):
        pinglunds[item1.text()]=item2.text()[3:]
    print(pinglunds)
    return user_star,zhuce_shijian,pinglunds
def get_html1(url):
    headers['Referer'] = headers['Referer'].format(url = url )
    response1 = requests.get(url = url,headers = headers)
    doc1 = pq(response1.text)
    pinglun_didian =doc1('h6').items()
    pinglun_shijian = doc1('span.col-exp').items()
    pinglunds={}
    for item1,item2 in zip(pinglun_didian,pinglun_shijian):
        pinglunds[item1.text()]=item2.text()[3:]
    print(pinglunds)
    return pinglunds
def ReadCSV(filename):
    datas = []
    dicts = {}
    with open(filename, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的文件
        # header = next(csv_reader)        # 读取第一行每一列的标题
        for rows in csv_reader:
            if rows[1][0:4] !='http':
                continue
            datas.append(rows[0])
            dicts[rows[0]] = rows[1]
        return datas,dicts

if __name__ =='__main__':
    datas,dicts = ReadCSV('获取店铺评论测试.csv')
    count = 1
    for data in datas:
        print("用户名称",data, "用户id",dicts[data].split('/')[4])
        with open('./获取用户个人评论.csv', 'a', newline='', encoding='utf-8') as out:
            csv_write = csv.writer(out, dialect='excel')
            if count ==1:
                #csv_write.writerow(["用户名称", "用户id","用户星级",'注册时间',"评论"])
                count-=1
            url = dicts[data]
            user_star,zhuceshijian,pinglunds = get_html(url)
            for i in range(2,20):
                pinglunds1 = get_html1(url+'/reviews?pg={pg}&reviewCityId=0&reviewShopType=0&c=0&shopTypeIndex=0'.format(pg = i))
                if not pinglunds1:
                    break
                if len(pinglunds1) == 1:
                    break
                pinglunds.update(pinglunds1)
                time.sleep(random.randint(1, 3))
            csv_write.writerow([data, dicts[data].split('/')[4], user_star, zhuceshijian, pinglunds])
            time.sleep(random.randint(2,4))
