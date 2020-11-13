import requests,csv,time,random

headers = {
    'referer': 'https://m.ctrip.com/webapp/you/place/2.html?ishideheader=true&from=https%3A%2F%2Fm.ctrip.com%2Fhtml5%2F',
    'cookie': '_RSG=Y4KLkMSeAD1DgV1P2h7XcB; _RDG=287c0a14105a902b0729ddfe0780e234aa; _RGUID=134aa1c5-ae55-4122-b9a1-1eb09905fa8d; _ga=GA1.2.1029762715.1600847787; MKT_CKID=1600847787249.hu6g2.yzp0; __utmz=1.1600847824.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); GUID=09031037311263378885; nfes_isSupportWebP=1; manualclose=1; __utmc=1; ibu_h5_lang=en; ibu_h5_local=en-us; __utma=1.1029762715.1600847787.1603864663.1603873149.3; _bfi=p1%3D290546%26p2%3D290564%26v1%3D79%26v2%3D77; Session=SmartLinkCode=U123474&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=&SmartLinkLanguage=zh; _jzqco=%7C%7C%7C%7C1603864615217%7C1.1016133315.1600847787244.1603873202858.1603949236497.1603873202858.1603949236497.undefined.0.0.33.33; __zpspc=9.6.1603949236.1603949236.1%232%7Cwww.sogou.com%7C%7C%7C%25E6%2590%25BA%25E7%25A8%258B%7C%23; _pd=%7B%22r%22%3A14%2C%22d%22%3A106%2C%22_d%22%3A92%2C%22p%22%3A106%2C%22_p%22%3A0%2C%22o%22%3A108%2C%22_o%22%3A2%2C%22s%22%3A108%2C%22_s%22%3A0%7D; _gid=GA1.2.342222326.1604920392; _gat=1; _RF1=39.170.26.194; _bfa=1.1600847784259.4ba1tm.1.1603873137302.1604920402389.7.94.214059',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'upgrade-insecure-requests': '1'
}
data = {
    'categoryId': '0',
    'commentScore': '',
    'count': '20',
    'districtId': '14',
    'fromChannel': '2',
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
    'index': '1',
    'isLibertinism': 'false',
    'lat': '0',
    'level2ThemeId': '0',
    'locationDistrictId': '0',
    'locationFilterDistance': '300',
    'locationFilterId': '0',
    'locationFilterType':'0',
    'lon': '0',
    'scene': "",
    'showAgg': 'true',
    'showNewVersion': 'true',
    'sightLevels': [],
    'sortType': '0',
    'sourceFrom': "sightlist",
    'themeId': '0',
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
