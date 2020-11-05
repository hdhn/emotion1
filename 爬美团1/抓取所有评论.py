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
    'Cookie':'_lxsdk_cuid=17289f6f39f0-0379aadb1ad974-335e4f7a-240000-17289f6f3a0c8; __mta=218930726.1591452565410.1591452565410.1591452565410.1; _hc.v=3becfc73-dec1-7e6e-5860-26583f0257ef.1591453491; iuuid=319626F6C2BFC8D402FE01069A408CA17291811E48548B1BFF66645D2CE70055; cityname=%E5%8C%97%E4%BA%AC; _lxsdk=319626F6C2BFC8D402FE01069A408CA17291811E48548B1BFF66645D2CE70055; client-id=7112cfcf-0a38-4442-8981-5699004a1939; ci=1; rvct=1%2C40%2C42%2C59%2C55%2C50%2C10%2C52%2C20%2C114%2C108; uuid=eed960c1-f1b7-4e98-b2a4-14c6499cf796; lat=39.879555; lng=116.473447; _lxsdk_s=172c6a1f245-581-827-0c6%7C%7C4',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3765.400 QQBrowser/10.6.4153.400'
}
filename = './店铺信息测试.csv'
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
    url1 ='https://www.meituan.com/meishi/api/poi/getMerchantComment?uuid=d65acdaf-7141-4690-9eda-67bcd7279e68&platform=1&partner=126&originUrl={url}&riskLevel=1&optimusCode=10&id={kk}'
    url2=url1.format(url = url,kk=p_id)
    fp = open("./美团评论13.csv",'a',newline = '',encoding='utf-8-sig')
    writer = csv.writer(fp)#我要写入
    #写入内容
    writer.writerow((("区域", dict1[p_id].area, "餐饮类型", dict1[p_id].food_type, "店铺id", dict1[p_id].poiId, "店铺名称", dict1[p_id].name, "经度", dict1[p_id].longitude, "纬度", dict1[p_id].latitude)))
    print("区域", dict1[p_id].area, "餐饮类型", dict1[p_id].food_type, "店铺id", dict1[p_id].poiId, "店铺名称", dict1[p_id].name, "经度", dict1[p_id].longitude, "纬度", dict1[p_id].latitude)
    writer.writerow(("用户","星级","评论"))#运行一次
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
                result = (name,star/10,comment)
                writer.writerow(result)
                # print(name,star/10,comment)
        except:
            print(response.url)
            print(response.text)
            a = input("请按enter键继续")
            if a=='1':
                break
        #exit()
    fp.close()