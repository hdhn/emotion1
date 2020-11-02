import requests,csv,time,re,json,zlib,base64,os,urllib,random
from urllib.parse import quote
class store():
    def __init__(self,area, food_type,poiId,name,longitude,latitude):
        self.area=area
        self.food_type=food_type
        self.poiId=poiId
        self.name=name
        self.longitude=longitude
        self.latitude=latitude
headers = {
    'Cookie':'_lxsdk_cuid=172d6562711c8-0b4880326e2ec7-34594f7d-e1000-172d65627123; __mta=151926022.1592733870984.1592733870984.1592733870984.1; ci=1; rvct=1; _hc.v=8059fb8a-9dd1-78a7-1fef-b419ea26fb76.1592733889; client-id=db361565-7d4e-43e0-ad4d-6feb839feedf; _lxsdk=172d6562711c8-0b4880326e2ec7-34594f7d-e1000-172d65627123; uuid=aa1c571f-3a25-4281-bed1-7b5c43f9f967; _lx_utm=utm_source%3Dwww.sogou%26utm_medium%3Dorganic; lat=40.474866; lng=116.867035; _lxsdk_s=17384fe3a7c-423-9c2-8a1%7C%7C10',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3756.400 QQBrowser/10.5.4043.400'
}
filename = './店铺信息测试1.csv'
#a =[]
dict1 = {}
datas = []
with open(filename,'r',encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的文件
    #header = next(csv_reader)        # 读取第一行每一列的标题
    for rows in csv_reader:
        datas.append(rows[5])
        #a.append(store(rows[1],rows[3],rows[5],rows[7],rows[9],rows[11]))
        dict1[rows[5]]=store(rows[1],rows[3],rows[5],rows[7],rows[9],rows[11])
        #print(a[0])
        #print(dict1[rows[5]])
        #exit()
    #print(datas)
    #exit()
for p_id in datas:
    target_url = 'https://www.meituan.com/meishi/{p_id}/'
    url = target_url.format(p_id=p_id)
    url1 ='https://www.meituan.com/meishi/api/poi/getMerchantComment?uuid=0e4f20a9-9294-48b0-be94-73952de2acdd&platform=1&partner=126&originUrl={url}&riskLevel=1&optimusCode=10&id={kk}'
    url2=url1.format(url = url,kk=p_id)
    fp = open("./美团评论24.csv",'a',newline = '',encoding='utf-8-sig')
    writer = csv.writer(fp)#我要写入
    #写入内容
    writer.writerow((("区域", dict1[p_id].area, "餐饮类型", dict1[p_id].food_type, "店铺id", dict1[p_id].poiId, "店铺名称", dict1[p_id].name, "经度", dict1[p_id].longitude, "纬度", dict1[p_id].latitude)))
    print("区域", dict1[p_id].area, "餐饮类型", dict1[p_id].food_type, "店铺id", dict1[p_id].poiId, "店铺名称", dict1[p_id].name, "经度", dict1[p_id].longitude, "纬度", dict1[p_id].latitude)
    writer.writerow(("用户","星级","评论时间","评论"))#运行一次
    for num in range(0,10000,10):
        print("正在爬取%s条。。。。。"%num)
        ajax_url = url2+'&userId=&offset={n}&pageSize=10&sortType=1'
        aurl =ajax_url.format(n=num)
        #print(aurl)
        response = requests.get(url=aurl,headers = headers)
        # print(response.text)
        # print(response.url)
        time.sleep(random.randint(1,3))
        try:
            for item in response.json()["data"]["comments"]:
                name = item["userName"]
                star = item["star"]
                comment = item["comment"]
                commentTime = int(item["commentTime"])
                time_local = time.localtime(commentTime/1000)
                # 转换成新的时间格式(2016-05-05 20:28:54)
                dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
                result = (name,star/10,dt,comment)
                writer.writerow(result)
                # print(name,star/10,comment)
        except TypeError:
            break
        except KeyError:
            print(response.url)
            verifyPageUrl = response.json()["customData"]["verifyPageUrl"]

            print(response.json()["customData"]["verifyPageUrl"])
            input("请按enter键继续")
        #exit()
    fp.close()