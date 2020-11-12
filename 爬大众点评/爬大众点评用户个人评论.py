import sys
import os
import re
import requests,csv
from pyquery import PyQuery as pq
import time,random

headers = {
    'Cookie':'cy=3; cye=hangzhou; _lxsdk_cuid=1753f165f9ec8-0cb558ba6b0e3a-6b111b7e-144000-1753f165f9fbe; _lxsdk=1753f165f9ec8-0cb558ba6b0e3a-6b111b7e-144000-1753f165f9fbe; _hc.v=9030c7fe-0b57-e105-ffa5-45d14dae3ce0.1603081232; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1603081232,1603081243; ll=7fd06e815b796be3df069dec7836c3df; ua=%E5%8B%BF%E5%BF%98%E5%BF%83%E5%AE%89_9104; ctu=7fc965fa839279cab50ca6c42a9981023b8d10bde71e72095032b366399a6fe8; uamo=13247877023; s_ViewType=10; lgtoken=037e83616-41e2-4b33-835e-e989377b892d; dper=a692dd00b59f6bb61dbee6cbd356f84ca9759ce61fd38cec1c34dd4af2833e9de75f06443554a7cc84eff48a876de8a9e6df65cf464542041203347a9d37996e57321a8b184aaf0e81b2930341fc1aa1d339073a49843ee04abd69fdff5db521; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1605157690; dplet=b5c99f1810d548ced5fc60e715c9890c; _lxsdk_s=175bad74914-497-771-fc6%7C%7C151',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36',
    'Referer': 'http://www.dianping.com/member/8540198/reviews'
}
url = 'http://www.dianping.com/member/8540198'
def get_html(url):
    response = requests.get(url =url,headers = headers)
    doc = pq(response.text)
    #print(doc)
    zhuce_shijian = doc("div.user-time>p").text()[-10:]
    user_star = doc("div.user-info>span").attr('class').split(' ')[1].replace('urr-rank','')
    print(user_star)
    print(zhuce_shijian)
    url1 = url+'/reviews'
    response1 = requests.get(url = url1,headers = headers)
    doc1 = pq(response1.text)
    pinglun_didian =doc1('h6').items()
    pinglun_shijian = doc1('span.col-exp').items()
    pinglunds={}
    for item1,item2 in zip(pinglun_didian,pinglun_shijian):
        pinglunds[item1.text()]=item2.text()[3:]
    print(pinglunds)
    return user_star,zhuce_shijian,pinglunds
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
    datas,dicts = ReadCSV('获取店铺评论.csv')
    count = 1
    for data in datas:
        print("用户名称",data, "用户id",dicts[data].split('/')[4])
        with open('./获取用户个人评论.csv', 'a', newline='', encoding='utf-8') as out:
            csv_write = csv.writer(out, dialect='excel')
            if count ==1:
                csv_write.writerow(["用户名称", "用户id","用户星级",'注册时间',"评论"])
                count-=1
            url = dicts[data]
            user_star,zhuceshijian,pinglunds = get_html(url)
            csv_write.writerow([data,dicts[data].split('/')[4],user_star,zhuceshijian,pinglunds])
            time.sleep(random.randint(3,5))