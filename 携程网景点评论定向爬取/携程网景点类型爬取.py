import requests,csv,time,random

headers = {
    'referer': 'https://m.ctrip.com/webapp/you/gspoi/sight/14.html?seo=0&navBarStyle=white&from=https%3A%2F%2Fm.ctrip.com%2Fwebapp%2Fyou%2Fplace%2F14.html%3Fishideheader%3Dtrue%26fromcitylist%3Dyes',
    'cookie': 'GUID=09031124410132639239; nfes_isSupportWebP=1; Union=OUID=&AllianceID=66672&SID=1693366&SourceID=&AppID=&OpenID=&exmktID=&createtime=1603895498&Expires=1604500298051; _ga=GA1.2.1881652236.1603895498; _gid=GA1.2.1049143587.1603895498; _RSG=8i4gonA5XG9cG307gzud9B; _RDG=28fb61a179866d212d221b036d9ee7fa01; _RGUID=942114ac-72a8-4b08-b267-e3da87003426; nfes_isSupportWebP=1; MKT_CKID=1603895549699.o4rnr.vbd2; MKT_CKID_LMT=1603895549699; MKT_Pagesource=PC; __utma=1.1881652236.1603895498.1603897456.1603897456.1; __utmc=1; __utmz=1.1603897456.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _bfi=p1%3D290546%26p2%3D290546%26v1%3D24%26v2%3D23; appFloatCnt=15; ibu_h5_lang=en; ibu_h5_local=en-us; _jzqco=%7C%7C%7C%7C1603895549857%7C1.2121701803.1603895549681.1603938441293.1603938441297.1603938441293.1603938441297.undefined.0.0.18.18; __zpspc=9.2.1603938441.1603938441.2%234%7C%7C%7C%7C%7C%23; _RF1=124.90.207.161; _pd=%7B%22r%22%3A7%2C%22d%22%3A68%2C%22_d%22%3A61%2C%22p%22%3A68%2C%22_p%22%3A0%2C%22o%22%3A70%2C%22_o%22%3A2%2C%22s%22%3A70%2C%22_s%22%3A0%7D; _bfa=1.1603895497895.17ad23o.1.1603895497976.1603938917056.3.36.214062',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
}
data = {
    'categoryId': '0',
    'commentScore': 'null',
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
    'locationFilterType': '0',
    'lon': '0',
    'scene': "",
    'showAgg': 'true',
    'showNewVersion': 'true',
    'sightLevels': [],
    'sortType': '0',
    'sourceFrom': "sightlist",
    'themeId': '0',
    'themeName': "",
    'ticketType': 'null',
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
    url ='https://m.ctrip.com/restapi/soa2/13342/json/getSightRecreationList?_fxpcqlniredt=09031124410132639239'
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
