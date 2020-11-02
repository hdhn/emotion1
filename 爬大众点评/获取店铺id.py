import requests,time,random
import csv
from pyquery import PyQuery as pq
headers ={
    'Cookie':'cy=3; cye=hangzhou; _lxsdk_cuid=1753bb608fbc8-0be3842885820b-6b111b7e-1fa400-1753bb608fcc8; _lxsdk=1753bb608fbc8-0be3842885820b-6b111b7e-1fa400-1753bb608fcc8; _hc.v=8429fd3f-f5ca-d6a9-fe0f-58cf71ca55b9.1603024588; s_ViewType=10; ua=%E5%8B%BF%E5%BF%98%E5%BF%83%E5%AE%89_9104; ctu=7fc965fa839279cab50ca6c42a998102e40f1aa3353081dc3b314009932e84da; fspop=test; _lx_utm=utm_source%3Dwww.sogou%26utm_medium%3Dorganic; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1603816072,1603890674,1603938685,1604062776; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1604063279; _lxsdk_s=175799786c3-203-0d-e4%7C%7C71; lgtoken=0928064c1-70d3-4422-a10c-899ff5372dc1; dplet=fc20a5e483dacf4e5fc831b85bab88aa; dper=87f016275af4b741d631840eb153fbe7ff4b110473113f9022841bce0011363c7b7e912b405f6a8e4ccb7404f6ebd19a6502024c520b3ec39f9fa2819217b1a291de83a356be1897ef93bbbc93fbc53b23a1e602d5853fde7698eb1a25bc2e70; ll=7fd06e815b796be3df069dec7836c3df; uamo=13247877023',
    'Host': 'www.dianping.com',
    'Accept-Encoding': 'gzip',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
}
headers1 = {
    'Cookie': 'cy=3; cye=hangzhou; _lxsdk_cuid=1753bb608fbc8-0be3842885820b-6b111b7e-1fa400-1753bb608fcc8; _lxsdk=1753bb608fbc8-0be3842885820b-6b111b7e-1fa400-1753bb608fcc8; _hc.v=8429fd3f-f5ca-d6a9-fe0f-58cf71ca55b9.1603024588; s_ViewType=10; ua=%E5%8B%BF%E5%BF%98%E5%BF%83%E5%AE%89_9104; ctu=7fc965fa839279cab50ca6c42a998102e40f1aa3353081dc3b314009932e84da; fspop=test; _lx_utm=utm_source%3Dwww.sogou%26utm_medium%3Dorganic; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1603816072,1603890674,1603938685,1604062776; dper=87f016275af4b741d631840eb153fbe7ff4b110473113f9022841bce0011363c7b7e912b405f6a8e4ccb7404f6ebd19a6502024c520b3ec39f9fa2819217b1a291de83a356be1897ef93bbbc93fbc53b23a1e602d5853fde7698eb1a25bc2e70; ll=7fd06e815b796be3df069dec7836c3df; uamo=13247877023; dplet=816cfa356bf6daf1577d81a434b61652; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1604063536; _lxsdk_s=175799786c3-203-0d-e4%7C%7C251',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36'
}
url ='http://www.dianping.com/hangzhou/ch10/p{page}'
url2 = 'http://www.dianping.com/shop/{shopid}/review_all'
flag=1
for page in range(1,30):
    url1 = url.format(page = page)
    html = requests.get(url = url1 ,headers = headers).text
    doc = pq(html)
    time.sleep(random.randint(1,3))
    with open('./获取店铺id.csv','a',newline='', encoding="utf-8") as fp:
        writer = csv.writer(fp)
        if flag==1:
            writer.writerow(('店铺id','店铺名称'))
            flag=0
        try:
            shophtml = doc('div.shop-all-list > ul >li>div.txt>div.tit>a')
            for i in shophtml:
                shopid = i.get('data-shopid')
                shoptitle = i.get('title')
                print(shopid,shoptitle)
                if shoptitle !=None:
                    url3 = url2.format(shopid = shopid)
                    response = requests.get(url=url3, headers=headers1)
                    time.sleep(random.randint(1,3))
                    # print(response.text)
                    doc = pq(response.text)
                    #print(doc('div.content>span.good'))
                    items = doc('div.content>span.good>a')
                    items1 = doc('div.content>span.bad>a')
                    list1 = []
                    for item in items:
                        print(item.text.replace(' ','').replace('\n',''))
                        list1.append(item.text.replace(' ','').replace('\n',''))
                    for item in items1:
                        print(item.text.replace(' ','').replace('\n',''))
                        list1.append(item.text.replace(' ','').replace('\n',''))
                    if not list1:
                        print(url3)
                        input("请按enter键继续")
                    writer.writerow((shopid,shoptitle,list1))
        except Exception as e:
            print(url1)
            print(e)
            input("请按enter键继续")


