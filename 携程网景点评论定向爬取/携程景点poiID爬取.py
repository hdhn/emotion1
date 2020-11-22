import requests,bs4,csv,time,random
from bs4 import BeautifulSoup

Headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
    'cookie':'_RSG=aD4dKHFsmP6SFwyET6xxUB; _RDG=2809306d21a059294127c70cd057146dfb; _RGUID=6670d8f4-549c-4364-b7bb-ec674ef3a3dc; _ga=GA1.2.1296828823.1603890718; MKT_CKID=1603890718214.2a7wa.3aid; StartCity_Pkg=PkgStartCity=17; __utmz=1.1603890752.1.1.utmcsr=dst.ctrip.com|utmccn=(referral)|utmcmd=referral|utmcct=/; GUID=09031158111725929500; nfes_isSupportWebP=1; nfes_isSupportWebP=1; U_TICKET_SELECTED_DISTRICT_CITY={%22value%22:{%22districtid%22:14%2C%22districtname%22:%22%E6%9D%AD%E5%B7%9E%22%2C%22isoversea%22:false%2C%22stage%22:%22inipageCity%22}%2C%22updateDate%22:1603895222893%2C%22createTime%22:1603895222724}; _RF1=124.90.207.26; _abtest_userid=ad690cd3-cf7c-41fd-b2c5-45d7b18a1c7e; Session=smartlinkcode=U130709&smartlinklanguage=zh&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=; Union=AllianceID=4901&SID=130709&OUID=&createtime=1605538205&Expires=1606143004577; MKT_CKID_LMT=1605538204598; _gid=GA1.2.1018221510.1605538205; MKT_Pagesource=PC; CRUISE_GPSAuthorized=0; _gat=1; __utma=1.1296828823.1603890718.1603895035.1605538523.3; __utmc=1; __utmt=1; __utmb=1.1.10.1605538523; ASP.NET_SessionSvc=MTAuNjEuMjIuMjQ0fDkwOTB8amlucWlhb3xkZWZhdWx0fDE1ODkwMDM3MTEwNzE; _bfa=1.1603890715334.ak4kk.1.1605535681403.1605538519473.17.65.10650014170; _bfs=1.6; _jzqco=%7C%7C%7C%7C1605538204671%7C1.450706088.1603890718212.1605538495705.1605538530940.1605538495705.1605538530940.undefined.0.0.18.18; __zpspc=9.4.1605538204.1605538530.3%233%7Cwww.sogou.com%7C%7C%7C%7C%23; appFloatCnt=20; _bfi=p1%3D290546%26p2%3D300119%26v1%3D65%26v2%3D64'
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