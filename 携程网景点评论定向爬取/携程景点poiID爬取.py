import requests,bs4,csv,time,random
from bs4 import BeautifulSoup

Headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
    'cookie':'nfes_isSupportWebP=1; _RF1=120.242.244.186; _RSG=bZ4c78WKf80ZttXK5bkAp8; _RDG=286d69e7d7f35d22c01cb65ae64d60b3c4; _RGUID=02295202-0798-48e5-8cca-ba5154877de3; MKT_CKID_LMT=1597581779253; MKT_CKID=1597581779252.8os2z.nesi; _ga=GA1.2.1370550959.1597581779; _gid=GA1.2.171091361.1597581779; MKT_Pagesource=PC; _bfs=1.15; _jzqco=%7C%7C%7C%7C1597581779418%7C1.845540725.1597581779250.1597641011880.1597641026290.1597641011880.1597641026290.undefined.0.0.20.20; __zpspc=9.2.1597640174.1597641026.11%234%7C%7C%7C%7C%7C%23; appFloatCnt=13; _bfi=p1%3D290546%26p2%3D290546%26v1%3D34%26v2%3D33; GUID=09031164410373614339; Union=OUID=&AllianceID=66672&SID=1693366&SourceID=&AppID=&OpenID=&exmktID=&createtime=1597641535&Expires=1598246335271; U_TICKET_SELECTED_DISTRICT_CITY=%7B%22value%22%3A%7B%22districtid%22%3A%2214%22%2C%22districtname%22%3A%22%E6%9D%AD%E5%B7%9E%22%2C%22isOversea%22%3Anull%7D%2C%22createTime%22%3A1597641560656%2C%22updateDate%22%3A1597641560656%7D; _bfa=1.1597581774848.3mrt5j.1.1597581774848.1597641560793.2.36.10650038368'
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
        for a in range(1,300):
            data['pidx'] = a
            r = requests.post(url,headers = Headers,json = data)
            print("正在爬取第%s页........"%a)
            #r.raise_for_status()
            #r.encoding = r.apparent_encoding
            yield r
    except:
        print("爬取失败")

def PresreveCSV(html):
    fp = open("./景点信息1.csv", 'a', newline='', encoding='utf-8-sig')
    writer = csv.writer(fp)  # 我要写入
    for items in html.json()["data"]["productList"]:
        try:
            print(items["poiId"],items['name'])
            writer.writerow((items["poiId"],items['name']))
        except KeyError:
            print("继续爬取下一个景点")
            continue
    fp.close()



def printUnivList():
    pass

def main():
    url = 'https://m.ctrip.com/restapi/soa2/14580/json/ProductSearch'
    htmls = getHTMLText(url)
    fp = open("./景点信息1.csv", 'a', newline='', encoding='utf-8-sig')
    writer = csv.writer(fp)  # 我要写入
    writer.writerow(("poiId", "景点名称"))
    fp.close()
    for html in htmls:
        PresreveCSV(html)
        time.sleep(random.randint(1, 3))
if __name__ == '__main__':
    main()