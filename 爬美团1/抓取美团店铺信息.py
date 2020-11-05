import requests,csv,time,re,json,zlib,base64,os,urllib
from urllib.parse import quote
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3754.400 QQBrowser/10.5.4020.400'
}
cityNames = {
                 # '北京':'http://bj.meituan.com/',
                 # '上海':'http://sh.meituan.com/',
                 # '深圳':'http://sz.meituan.com/',
                 # '广州':'http://gz.meituan.com/',
                 # '杭州':'http://hz.meituan.com/',
                 # '南京':'http://nj.meituan.com/',
                 # '成都':'http://cd.meituan.com/',
                 # '武汉':'http://wh.meituan.com/',
                 # '苏州':'http://su.meituan.com/',
                 # '重庆':'http://cq.meituan.com/',
                 # '天津':'http://tj.meituan.com/',
                 # '郑州':'http://zz.meituan.com/',
                 # '西安':'http://xa.meituan.com/',
                 # '长沙':'http://chs.meituan.com/',
                 # '宁波':'http://nb.meituan.com/',
                 # '佛山':'http://fs.meituan.com/',
                 # '青岛':'http://qd.meituan.com/',
                 # '合肥':'http://hf.meituan.com/',
                 # '济南':'http://jn.meituan.com/',
                 # '东莞':'http://dg.meituan.com/',
                 # '福州':'http://fz.meituan.com/',
                 # '无锡':'http://wx.meituan.com/',
                 # '厦门':'http://xm.meituan.com/',
                 # '珠海':'http://zh.meituan.com/',
                 '昆明':'http://km.meituan.com/'}
class MakeToken():
    """
    测试2020-6-21日可用
    仅作为学术交流！如有侵权，联系作者删除
    美团【餐馆列表】Token生成
    """

    def __init__(self, areaId, cityName, originUrl, page):
        self.areaId = areaId
        self.cityName = cityName
        self.originUrl = originUrl
        self.page = page
        self.uuid = '8f800f8a-a5bf-48e6-96df-334cc14ab61d'  # Demo c6eada3ffd8e444491e9.1555472928.3.0.0

    def join_sign(self):
        # 参数
        sign = 'areaId={areaId}&cateId=0&cityName={cityName}&dinnerCountAttrId=&optimusCode=10&originUrl={originUrl}&page={page}&partner=126&platform=1&riskLevel=1&sort=&userId=&uuid={uuid}'
        _str = sign.format(areaId=self.areaId, cityName=self.cityName, originUrl=self.originUrl+'meishi/', page=self.page,
                           uuid=self.uuid)
        sign = base64.b64encode(zlib.compress(bytes(json.dumps(_str, ensure_ascii=False), encoding="utf8")))
        sign = str(sign, encoding="utf8")
        return sign

    @property
    def join_token(self):
        str_json = {}
        str_json['rId'] = 100900
        str_json['ver'] = '1.0.6'
        str_json['ts'] = int(time.time()*1000)
        str_json['cts'] = int(time.time()*1000+50)
        str_json['brVD'] = [854,815]  #[1920, 315]
        str_json['brR'] = [[2048,1152],[2048,1112],24,24] #[[1920, 1080], [1920, 1057], 24, 24]
        str_json['bI'] = [self.originUrl+'meishi/',self.originUrl]
        str_json['mT'] = []
        str_json['kT'] = []
        str_json['aT'] = []
        str_json['tT'] = []
        str_json['aM'] = ''
        str_json['sign'] = self.join_sign()
        token_decode = zlib.compress(
            bytes(json.dumps(str_json, separators=(',', ':'), ensure_ascii=False), encoding="utf8"))
        token = str(base64.b64encode(token_decode), encoding="utf8")
        return token
def parse_html(data):
    """解析数据
    """
    # 细节信息
    detail_info = re.search(
        r'"detailInfo":\{"poiId":(\d+),"name":"(.*?)","avgScore":(.*?),"address":"(.*?)","phone":"(.*?)","openTime":"(.*?)","extraInfos":\[(.*?)\],"hasFoodSafeInfo":(.*?),"longitude":(.*?),"latitude":(.*?),"avgPrice":(\d+),"brandId":(\d+),"brandName":"(.*?)",".*?photos":{"frontImgUrl":"(.*?)","albumImgUrls":(.*?)},"recommended":(.*?),"crumbNav":(.*?),"prefer',
        data)
    if detail_info:
        longitude = detail_info.group(9)
        latitude = detail_info.group(10)
        poiId = detail_info.group(1)
        name = detail_info.group(2)
        # 面包屑抽离
        crumbNav = json.loads(detail_info.group(17))
        area = crumbNav[0].get('title')[:-2]
        food_type = crumbNav[2].get('title')[len(area):]
        print('区域: ', area, ' 餐饮类型: ', food_type)
        fp = open("./店铺信息7.csv", 'a', newline='', encoding='utf-8-sig')
        writer = csv.writer(fp)  # 我要写入
        # 写入内容
        writer.writerow(("区域", area, "餐饮类型", food_type, "店铺id", poiId, "店铺名称", name, "经度", longitude, "纬度", latitude))
        fp.close()
    #         print_str = """
    # 店铺ID: {poiId}
    # 餐馆名称: {name}
    # 经度: {longitude}
    # 纬度: {latitude}
    # ：""".format(poiId = poiId,name = name,longitude=longitude, latitude=latitude)
    #         print(print_str)
    else:
        print('数据信息失败')
if __name__ == '__main__':
    # 测试数据
    areaId = '0'
    for cityName in cityNames:
        originUrl = cityNames[cityName]
        originUrl1 = originUrl +'meishi/'
        #print(originUrl)
    # ssss = decode_token(token.join_token)
    # print(ssss)
    #     print(token.join_token)
        for page in range(1,60):
            token = MakeToken(areaId, cityName, originUrl, page)
            print(areaId, cityName, originUrl, page)
            url ='{originUrl}meishi/api/poi/getPoiList?cityName={cityName}&cateId=0&areaId=0&sort=&dinnerCountAttrId=&page={page}&userId=&uuid=d65acdaf-7141-4690-9eda-67bcd7279e68&platform=1&partner=126&originUrl={originUrl1}&riskLevel=1&optimusCode=10&_token={token}'.format(originUrl=originUrl,token=quote(token.join_token, 'utf-8'),cityName=quote(cityName, 'utf-8'),originUrl1=quote(originUrl1, 'utf-8'),page=page)
            #print(url)
            response = requests.get(url=url, headers=headers)
            print(response.text)
            try:
                for item in response.json()["data"]["poiInfos"]:
                    p_id = item["poiId"]
                    target_url = 'https://www.meituan.com/meishi/{p_id}/'
                    url = target_url.format(p_id=p_id)
                    response = requests.get(url, headers=headers)
                    #time.sleep(2)
                    data = response.text
                    #print(response.url)
                    #print(data)
                    #exit()
                    # 提取有效区域
                    data = re.search(r'12315消费争议(.*?)"dealList":', data, flags=re.DOTALL)
                    if data:
                        parse_html(data.group(1))
                    else:
                        print(response.url)
                        input("请按enter键继续")
                        # request_code = response.json()["request_code"]
                        # yanzhengurl = 'https://verify.meituan.com/v2/captcha?request_code={request_code}&action=spiderindefence&randomId=0.43945441023651055'.format(request_code=request_code)
                        # print('访问失效')
                        #os.system("pause")
                    print(p_id)
            except:
                input("请按enter键继续")
                    # url1 ='https://www.meituan.com/meishi/api/poi/getMerchantComment?uuid=d65acdaf-7141-4690-9eda-67bcd7279e68&platform=1&partner=126&originUrl={url}&riskLevel=1&optimusCode=10&id={kk}'
                    # url2=url1.format(url = url,kk=p_id)
                    # fp = open("./美团评论5.csv",'a',newline = '',encoding='utf-8-sig')
                    # writer = csv.writer(fp)#我要写入
                    # #写入内容
                    # writer.writerow(("用户","星级","评论"))#运行一次
                    # for num in range(0,500,10):
                    #     print("正在爬取%s条。。。。。"%num)
                    #     ajax_url = url2+'&userId=&offset={n}&pageSize=10&sortType=1'
                    #     aurl =ajax_url.format(n=num)
                    #     #print(aurl)
                    #     response = requests.get(url=aurl,headers = headers)
                    #     # print(response)
                    #     time.sleep(2)
                    #     try:
                    #         for item in response.json()["data"]["comments"]:
                    #             name = item["userName"]
                    #             star = item["star"]
                    #             comment = item["comment"]
                    #             result = (name,star/10,comment)
                    #             writer.writerow(result)
                    #             # print(name,star/10,comment)
                    #     except:
                    #         break
                    #     #exit()
                    # fp.close()