import requests,bs4,csv,time,random
from bs4 import BeautifulSoup

Headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
    'cookie':'nfes_isSupportWebP=1; _RF1=120.242.244.186; _RSG=bZ4c78WKf80ZttXK5bkAp8; _RDG=286d69e7d7f35d22c01cb65ae64d60b3c4; _RGUID=02295202-0798-48e5-8cca-ba5154877de3; _bfi=p1%3D290510%26p2%3D290510%26v1%3D2%26v2%3D1; MKT_CKID=1597581779252.8os2z.nesi; MKT_CKID_LMT=1597581779253; __zpspc=9.1.1597581779.1597581779.1%234%7C%7C%7C%7C%7C%23; _ga=GA1.2.1370550959.1597581779; _gid=GA1.2.171091361.1597581779; _gat=1; _jzqco=%7C%7C%7C%7C1597581779418%7C1.845540725.1597581779250.1597581779250.1597581779251.1597581779250.1597581779251.0.0.0.1.1; _bfa=1.1597581774848.3mrt5j.1.1597581774848.1597581774848.1.3; _bfs=1.3'
}
data = {
    'arg': {
        'channelType': '2',
        'collapseType':'0',
        'commentTagId': '0',
        'pageIndex': '1',
        'pageSize': '10',
        'poiId': '10558619',
        'sourceType': '1',
        'sortType': '3',
        'starType': '0'},
    'head': {
        'cid': "09031164410373614339",
        'ctok': "",
        'cver': "1.0",
        'lang': "01",
        'sid': "8888",
        'syscode': "09",
        'auth': "",
        'xsid': "",
        'extension': []}
}
data1 = {
    'arg': {
    'poiId':'10558619',
    'sourceType': '1'},
    'head': {
    'cid': "09031164410373614339",
    'ctok': "",
    'cver': "1.0",
    'lang': "01",
    'sid': "8888",
    'syscode': "09",
    'auth': "",
    'xsid': "",
    'extension': []}
}
def ReadCSV(filename):
    datas = []
    dicts = {}
    with open(filename, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的文件
        # header = next(csv_reader)        # 读取第一行每一列的标题
        for rows in csv_reader:
            datas.append(rows[0])
            dicts[rows[0]] = rows[1]
        return datas,dicts
def getHTMLText(url,url1,dicts,datas):
    try:
        for i in datas:
            data['arg']['poiId'] = i
            data1['arg']['poiId'] = i
            r1 = requests.post(url1, headers=Headers, json=data1)
            print("正在爬取 %s 的景点评论" %dicts[i])
            fp = open("./景点评论2.csv", 'a', newline='', encoding='utf-8-sig')
            writer = csv.writer(fp)  # 我要写入
            writer.writerow(("景点名称", dicts[i], "景点位置", r1.json()["result"]["poiInfo"]["address"]))
            writer.writerow(("用户ID", "用户昵称", "评论时间", "评论内容"))
            fp.close()
            for a in range(1,100):
                try:
                    data['arg']['pageIndex'] = str(a)
                    r = requests.post(url, headers=Headers, json=data)
                    if r.json()["result"]["items"] == None:
                        break
                    print("正在爬取第%s页........" % a)
                    # print(r.text)
                    # r.raise_for_status()
                    # r.encoding = r.apparent_encoding
                    yield r
                except:
                    break
    except:
        input("按enter键继续")
def PreserveCSV(html):
    fp = open("./景点评论2.csv", 'a', newline='', encoding='utf-8-sig')
    writer = csv.writer(fp)  # 我要写入
    try:
        for items in html.json()["result"]["items"]:
            try:
                #print(items['publishTime'][6:19])
                timestamp = int(items['publishTime'][6:16])
                #转换成localtime
                time_local = time.localtime(timestamp)
                #转换成新的时间格式(2016-05-05 )
                dt = time.strftime("%Y-%m-%d",time_local)
                print(items["userInfo"]["userId"], items["userInfo"]["userNick"],dt, items['content'])
                writer.writerow((items["userInfo"]["userId"], items["userInfo"]["userNick"],dt,items['content']))
            except TypeError:
                #input("按enter键继续")
                print("爬取下一条评论。。。。。")
                continue
    except TypeError:
        #print(html.text)
        input("请按enter键继续")
    fp.close()
def main():
    filename = './景点信息测试.csv'
    url = 'https://m.ctrip.com/restapi/soa2/13444/json/getCommentCollapseList?_fxpcqlniredt=09031164410373614339'
    url1 = 'https://m.ctrip.com/restapi/soa2/13444/json/getPoiCommentInfoWithHotTag?_fxpcqlniredt=09031164410373614339'
    datas,dicts = ReadCSV(filename)
    htmls = getHTMLText(url,url1, dicts, datas)
    for html in htmls:
        #print(html.text)
        PreserveCSV(html)
        time.sleep(random.randint(1, 3))

if __name__ == '__main__':
    main()