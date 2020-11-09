import requests,csv,time,random

headers = {
    'referer': 'https://m.ctrip.com/webapp/you/gspoi/sight/14.html?seo=0&navBarStyle=white&from=https%3A%2F%2Fm.ctrip.com%2Fwebapp%2Fyou%2Fplace%2F14.html%3Fishideheader%3Dtrue%26fromcitylist%3Dyes',
    'cookie': 'Session=SmartLinkCode=U123474&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=&SmartLinkLanguage=zh; _RSG=aD4dKHFsmP6SFwyET6xxUB; _RDG=2809306d21a059294127c70cd057146dfb; _RGUID=6670d8f4-549c-4364-b7bb-ec674ef3a3dc; _ga=GA1.2.1296828823.1603890718; MKT_CKID=1603890718214.2a7wa.3aid; StartCity_Pkg=PkgStartCity=17; __utmz=1.1603890752.1.1.utmcsr=dst.ctrip.com|utmccn=(referral)|utmcmd=referral|utmcct=/; GUID=09031158111725929500; nfes_isSupportWebP=1; nfes_isSupportWebP=1; __utma=1.1296828823.1603890718.1603890752.1603895035.2; U_TICKET_SELECTED_DISTRICT_CITY={%22value%22:{%22districtid%22:14%2C%22districtname%22:%22%E6%9D%AD%E5%B7%9E%22%2C%22isoversea%22:false%2C%22stage%22:%22inipageCity%22}%2C%22updateDate%22:1603895222893%2C%22createTime%22:1603895222724}; _jzqco=%7C%7C%7C%7C1603890718268%7C1.450706088.1603890718212.1603895248758.1603897655508.1603895248758.1603897655508.undefined.0.0.15.15; __zpspc=9.3.1603897655.1603897655.1%232%7Cwww.sogou.com%7C%7C%7C%25E6%2590%25BA%25E7%25A8%258B%7C%23; appFloatCnt=15; _gid=GA1.2.349959731.1604811374; Union=OUID=&AllianceID=66672&SID=1693366&SourceID=&AppID=&OpenID=&exmktID=&createtime=1604811374&Expires=1605416174152; _RF1=124.90.207.49; ibu_h5_lang=en; ibu_h5_local=en-us; _gat=1; _pd=%7B%22r%22%3A8%2C%22d%22%3A95%2C%22_d%22%3A87%2C%22p%22%3A95%2C%22_p%22%3A0%2C%22o%22%3A98%2C%22_o%22%3A3%2C%22s%22%3A99%2C%22_s%22%3A1%7D; _bfa=1.1603890715334.ak4kk.1.1603895035648.1604811941174.4.42.214062',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
}
data = {
    'categoryId': 0,
    'commentScore': '',
    'count': 20,
    'districtId': 14,
    'fromChannel': 2,
    'fromNearby': "",
    'head': {
        'auth': "",
        'cid': "09031124410132639239",
        'ctok': "",
        'cver': "1.0",
        'extension': [],
        'lang': "01",
        'sid': "8888",
        'syscode': "09",
        'xsid': ""
    },
    'hideTop': 'false',
    'hiderank': "",
    'index': 1,
    'isLibertinism': 'false',
    'lat': 0,
    'level2ThemeId': 0,
    'locationDistrictId': 0,
    'locationFilterDistance': 300,
    'locationFilterId': 0,
    'locationFilterType':0,
    'lon': 0,
    'scene': "",
    'showAgg': 'true',
    'showNewVersion': 'true',
    'sightLevels': [],
    'sortType': 0,
    'sourceFrom': "sightlist",
    'themeId': 0,
    'themeName': "",
    'ticketType': '',
}
def getHTMLText(url):
    try:
        for a in range(1,300):
            data['index'] = a
            r = requests.post(url,headers = headers,json = data)
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
    for items in html.json()["result"]["sightRecreationList"]:
        try:
            print(items["poiId"],items['name'],items['resourceTags'])
            writer.writerow((items["poiId"],items['name'],items['resourceTags']))
        except KeyError:
            print("继续爬取下一个景点")
            continue
    fp.close()



def printUnivList():
    pass

def main():
    url ='https://m.ctrip.com/restapi/soa2/13342/json/getSightRecreationList?_fxpcqlniredt=09031158111725929500'
    htmls = getHTMLText(url)
    fp = open("./景点类型标签.csv", 'a', newline='', encoding='utf-8-sig')
    writer = csv.writer(fp)  # 我要写入
    writer.writerow(("poiId", "景点名称","景点类型"))
    fp.close()
    for html in htmls:
        PresreveCSV(html)
        time.sleep(random.randint(1, 3))
if __name__ == '__main__':
    main()
