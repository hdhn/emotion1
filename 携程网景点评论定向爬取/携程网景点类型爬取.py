import requests,csv,time,random

Headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
    'cookie':'GUID=09031124410132639239; nfes_isSupportWebP=1; _ga=GA1.2.1881652236.1603895498; _RSG=8i4gonA5XG9cG307gzud9B; _RDG=28fb61a179866d212d221b036d9ee7fa01; _RGUID=942114ac-72a8-4b08-b267-e3da87003426; nfes_isSupportWebP=1; MKT_CKID=1603895549699.o4rnr.vbd2; __utmz=1.1603897456.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ibu_h5_lang=en; ibu_h5_local=en-us; MKT_Pagesource=PC; GUID=09031154212356017799; Union=OUID=&AllianceID=66672&SID=1693366&SourceID=&AppID=&OpenID=&exmktID=&createtime=1605885032&Expires=1606489831859; __utma=1.1881652236.1603895498.1603897456.1605885070.2; __zpspc=9.3.1605885015.1605885081.4%234%7C%7C%7C%7C%7C%23; _jzqco=%7C%7C%7C%7C1605885015252%7C1.2121701803.1603895549681.1605885076648.1605885081104.1605885076648.1605885081104.undefined.0.0.22.22; appFloatCnt=21; _gid=GA1.2.132914786.1606048469; _RF1=124.90.207.128; _pd=%7B%22r%22%3A10%2C%22d%22%3A122%2C%22_d%22%3A112%2C%22p%22%3A122%2C%22_p%22%3A0%2C%22o%22%3A124%2C%22_o%22%3A2%2C%22s%22%3A124%2C%22_s%22%3A0%7D; U_TICKET_SELECTED_DISTRICT_CITY=%7B%22value%22%3A%7B%22districtid%22%3A%2214%22%2C%22districtname%22%3A%22%E6%9D%AD%E5%B7%9E%22%2C%22isOversea%22%3Anull%7D%2C%22createTime%22%3A1606058114626%2C%22updateDate%22%3A1606058114626%7D; _bfa=1.1603895497895.17ad23o.1.1603938917056.1606058114700.6.62.10650038368'
}
data = {
    'head': {
        'cid': "09031164410373614339",
        'syscode': "999"},
    'ver': "8.3.2",
    'debug': 'false',
    'pageid': "10650038368",
    'contentType': "json",
    'clientInfo':{
        'pageId': "10650038368",
        'platformId': 'null',
        'crnVersion': "2020-08-12 13:23:37",
        'location': {
                'lat': "",
                'lon': "",
                'cityId': "",
                'locatedCityId': "",
                'districtId': "14",
                'locatedDistrictId': "",
                'cityType': ""},
        'locale': "zh-CN",
        'currency': "CNY"},
    'bizLineType': '1',
    'pshowcode': "",
    'needUpStream': 'false',
    'pidx': '1',
    'sort': "1",
    'qsids': "",
    'psize':'20',
    'imgsize': "C_568_320",
    'extras': [],
    'traceid': "b57ba0cb-a287-d810-6b14-159764255552"
}
def getHTMLText(url):
    try:
        for a in range(1,150):
            data['index'] = str(a)
            r = requests.post(url,headers = Headers,json = data)
            print("正在爬取第%s页........"%a)
            #r.raise_for_status()
            #r.encoding = r.apparent_encoding
            yield r
    except:
        print("爬取失败")

def PresreveCSV(html):
    print(html.text)
    fp = open("./景点类型标签.csv", 'a', newline='', encoding='utf-8-sig')
    writer = csv.writer(fp)  # 我要写入
    for items in html.json()["data"]["productList"]:
        try:
            print(items["poiId"],items['name'],items['score'],items['productTags'])
            text = []
            for i in items['productTags']:
                text.append(i['text'])
            writer.writerow((items["poiId"],items['name'],items['score'],text))
        except KeyError:
            print("继续爬取下一个景点")
            continue
    fp.close()



def printUnivList():
    pass

def main():
    url ='https://m.ctrip.com/restapi/soa2/14580/json/ProductSearch'
    htmls = getHTMLText(url)
    fp = open("./景点类型标签.csv", 'a', newline='', encoding='utf-8-sig')
    writer = csv.writer(fp)  # 我要写入
    writer.writerow(("poiId", "景点名称","景点评分","景点标签"))
    fp.close()
    for html in htmls:
        PresreveCSV(html)
        time.sleep(random.randint(1, 3))
if __name__ == '__main__':
    main()
