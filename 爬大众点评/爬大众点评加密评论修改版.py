#!/usr/bin/env python
# encoding: utf-8
"""
@version: v1.0
@author: W_H_J
@license: Apache Licence
@contact: 415900617@qq.com
@software: PyCharm
@file: dazhongdianping.py
@time: 2018/12/19 17:45
@describe: 大众点评评论抓取-解析
"""
import sys
import os
import re,csv
import requests
from pyquery import PyQuery as pq
import random,time

# sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
# sys.path.append("..")

header_pinlun = {
    'Cookie':'Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1614262781; ll=7fd06e815b796be3df069dec7836c3df; uamo=13247877023; _hc.v=417c4a48-2668-51f5-a7e5-ea0db3d6b53c.1611638037; ctu=fe93aeb2070b2cfc0f27a74d6779976cb85a1e1978a70374697722afc51c6db3; dper=3497c27c2d09fc4d9fae3b8c9ec8d30966a3b939c9b3d1cab842a94dcb8384246d0e2f120ca64d787abef9a69d51b131e53292512e4f95b7c47f5c54e2a81235fc7c9c339e14124bb18f86bbf4b4f24fd8a7af477644bab04e2f49230d315450; _lxsdk_cuid=1773d1cd959c8-04432c5d347403-71415a3a-240000-1773d1cd95923; s_ViewType=10; _lxsdk=1773d1cd959c8-04432c5d347403-71415a3a-240000-1773d1cd95923; fspop=test; dplet=9f8e6db6560eb2b9315e0b795a6019f4; ua=%E5%8B%BF%E5%BF%98%E5%BF%83%E5%AE%89_9104; cye=hangzhou; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1613574121,1613714650,1613981655,1614142146; cy=3; _lxsdk_s=177d98f23f6-81b-aee-166%7C%7C109',
    'Host': 'www.dianping.com',
    'Accept-Encoding': 'gzip',
    'Referer': 'http://www.dianping.com/shop/{shopid}/review_all',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
}

header_css = {
    'Host': 's3plus.meituan.net',
    'Accept-Encoding': 'gzip',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'

}


# 0-详情页
def get_msg(shopid,page):
    """
    url: http://www.dianping.com/shop/+ 商铺ID +/review_all
    :return:
    """
    # url = "http://www.dianping.com/shop/110620927/review_all"
    url = "http://www.dianping.com/shop/{shopid}/review_all/p{page}".format(shopid = shopid,page = page-1)
    # url = "https://www.dianping.com/shop/77307732/review_all"
    header_pinlun['Referer'] = header_pinlun['Referer'].format(shopid = shopid)
    html = requests.get(url, headers=header_pinlun)
    print("1 ===> STATUS", html.status_code)
    doc = pq(html.text)
    try:
        print(doc("head >link")[3].get('href'))
    except:
        print(url)
        return 0
    # 解析每条评论
    pinglunLi = doc("div.reviews-items > ul > li").items()
    if not doc("div.reviews-items > ul > li"):
        print("该页面没有评论")
        return 0

    """
    调用评论里的css样式处理和加密字体svg处理
    :return:
    dict_svg_text: svg整个加密字库，以字典形式返回
    list_svg_y：svg背景中的<path>标签里的[x,y]坐标轴，以[x,y]形式返回
    dict_css_x_y：css样式中，每个加密字体的<span> 标签内容，用于匹配dict_svg_text 中的key，以字典形式返回
    """
    dict_svg_text, list_svg_y, dict_css_x_y = css_get(doc)

    for data in pinglunLi:
        # 用户名
        userName = data("div.main-review > div.dper-info > a").text()
        if not userName:
            return 2
        # 用户ID链接
        try:
            userID = "http://www.dianping.com" + data("div.main-review > div.dper-info > a").attr("href")
        except:
            userID ="匿名用户"
        # 用户评分星级[10-50]
        try:
            startShop = str(data("div.review-rank > span").attr("class")).split(" ")[1].replace("sml-str", "")
        except:
            startShop = '0'#用户评分不存在
        # 用户描述：机器：非常好 环境：非常好 服务：非常好 人均：0元
        describeShop = data("div.review-rank > span.score").text()
        # 关键部分，评论HTML,待处理，评论包含隐藏部分和直接展示部分，默认从隐藏部分获取数据，没有则取默认部分。（查看更多）
        pinglun = data("div.review-words.Hide").html()
        #print(pinglun)
        try:
            len(pinglun)
        except:
            pinglun = data("div.review-words").html()
        # 该用户喜欢的美食
        loveFood = data("div.main-review > div.review-recommend").text()
        # 发表评论的时间
        pinglunTime = data("div.main-review > div.misc-info.clearfix > span.time").text()
        print("userName:", userName)
        print("userID:", userID)
        print("startShop:", startShop)
        print("describeShop:", describeShop)
        print("loveFood:", loveFood)
        print("pinglunTime:", pinglunTime)
        print("pinglun:", css_decode(dict_css_x_y, dict_svg_text, list_svg_y, pinglun))
        print("*" * 100)
        pinluncontent = css_decode(dict_css_x_y, dict_svg_text, list_svg_y, pinglun)
        out = open('./获取店铺评论4.csv', 'a', newline='', encoding='utf-8')
        # 设定写入模式
        csv_write = csv.writer(out, dialect='excel')
        if pinglunTime[0:4]=='2020':
            csv_write.writerow([userName,userID,startShop,describeShop,loveFood,pinglunTime,pinluncontent])
        elif pinglunTime[0:4]=='2019':
            return 2
        out.close()
        print("successful insert csv!")
    return 1


# 1-评论隐含部分字体css样式, 获取svg链接，获取加密汉字background
def css_get(doc):
    css_link = "http:" + doc("head >link")[3].get('href')#doc("head > link:nth-child(11)").attr("href")
    background_link = requests.get(css_link, headers=header_css)
    r = r'svgmtsi.*?background-image: url(.*?);'
    matchObj = re.compile(r, re.I)
    try:
        svg_link = matchObj.findall(background_link.text)[0].replace(")", "").replace("(", "http:")
        print(svg_link)
        """
        svg_text() 方法：请求svg字库，并抓取加密字
        dict_svg_text: svg整个加密字库，以字典形式返回
        list_svg_y：svg背景中的<path>标签里的[x,y]坐标轴，以[x,y]形式返回
        """
        dict_avg_text, list_svg_y = svg_text(svg_link)
        """
        css_dict() 方法：生成css样式中background的样式库
        dict_css: 返回css字典样式
        """
        dict_css = css_dict(background_link.text)
        return dict_avg_text, list_svg_y, dict_css
    except:
        input("24小时内无法访问大众点评评论")


# 2-字体库链接
def svg_text(url):
    html = requests.get(url)
    dict_svg, list_y = svg_dict(html.text)
    #print(dict_svg, list_y)
    return dict_svg, list_y


# 3-生成svg字库字典
def svg_dict(csv_html):
    svg_text_r = r'<text x="0" y="(.*?)">(.*?)</text>'
    svg_text_re = re.findall(svg_text_r, csv_html)
    #print(svg_text_re)
    dict_avg = {}
    # 生成svg加密字体库字典
    count = 0
    for data in svg_text_re:
        dict_avg[count] = list(data[1])
        count+=1
    """
    重点：http://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/74d63812e5b327d850ab4a8782833d47.svg
        svg <path> 标签里内容对应css样式中background的y轴参数，小于关系，
        如果css样式中的background的y参数小于 svg_y_re 集合中最小的数，则向上取y轴，('18', 'M0', '748', 'H600')，
        如.gqi4j {background: -98.0px -745.0px;} 中的y-745，取正数745，小于748，则对应加密字库实际y轴为748，对应的18就是<textPath>中的x轴
    """
    svg_y_r = r'<text x="0" y="(.*?)">(.*?)</text>'
    svg_y_re = re.findall(svg_y_r, csv_html)
    list_y = []
    # 存储('18', 'M0', '748', 'H600') eg:(x坐标，未知，y坐标，未知)
    i = 0
    for data in svg_y_re:
        list_y.append([i, data[0]])
        i+=1
    return dict_avg, list_y


# 4-生成css字库字典
def css_dict(html):
    css_text_r = r'.(.*?){background:(.*?)px (.*?)px;}'
    css_text_re = re.findall(css_text_r, html)
    dict_css = {}
    for data in css_text_re:
        """
        加密字库.gqi4j {background: -98.0px -745.0px;}与svg文件对应关系，x/14，就是svg文件加密字体下标
        y，原样返回，需要在svg函数中做处理
        """
        x = int(float(data[1]) / -14)
        """
        字典参数：{css参数名：(background-x,background-y,background-x/14,background-y)}
        """
        dict_css[data[0]] = (data[1], data[2], x, data[2])
    #print(dict_css)
    return dict_css


# 5-最终评论汇总
def css_decode(css_html, svg_dict, svg_list, pinglun_html):
    """
    :param css_html: css 的HTML源码
    :param svg_dict: svg加密字库的字典
    :param svg_list: svg加密字库对应的坐标数组[x, y]
    :param pinglun_html: 评论的HTML源码，对应0-详情页的评论，在此处理
    :return: 最终合成的评论
    """
    css_dict_text = css_html
    csv_dict_text, csv_dict_list = svg_dict, svg_list
    # 处理评论源码中的span标签，生成字典key
    pinglun_text = pinglun_html.replace('<svgmtsi class="', ',').replace('"/>', ",").replace('">', ",")
    pinglun_list = [x for x in pinglun_text.split(",") if x != '']
    pinglun_str = []
    for msg in pinglun_list:
        # 如果有加密标签
        if msg in css_dict_text:
            # 参数说明：[x,y] css样式中background 的[x/14，y]
            x = int(css_dict_text[msg][2])
            y = -float(css_dict_text[msg][3])
            # 寻找background的y轴比svg<path>标签里的y轴小的第一个值对应的坐标就是<textPath>的href值
            for g in csv_dict_list:
                if y < int(g[1]):
                    # print(g)
                    # print(csv_dict_text[g[0]][x])
                    pinglun_str.append(csv_dict_text[g[0]][x])
                    break
        # 没有加密标签
        else:
            pinglun_str.append(msg.replace("\n", ""))
    str_pinglun = ""
    for x in pinglun_str:
        str_pinglun += x
    # 处理特殊标签
    #print(str_pinglun)
    dr2 = re.compile(r'<.*?>', re.S)
    dr = re.compile(r'<img.*?alt="', re.S)
    dr3 = re.compile(r'&(.*?);', re.S)
    dd = dr.sub('', str_pinglun)
    dd2 = dr2.sub('', dd)
    str_pinglun = dr3.sub('', dd2)
    str_pinglun = str_pinglun.replace(' ','').replace('收起评价','')
    return str_pinglun
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

if __name__ == '__main__':
    file_name = './获取店铺id1测试.csv'
    datas, dicts = ReadCSV(file_name)
    for data in datas:
        out = open('./获取店铺评论4.csv', 'a', newline='', encoding='utf-8')
        # 设定写入模式
        csv_write = csv.writer(out, dialect='excel')
        csv_write.writerow(["店铺名称", "店铺id"])
        csv_write.writerow([dicts[data], data])
        csv_write.writerow(["userName", "userID", "startShop", "describeShop", "loveFood", "pinglunTime", "pinglun"])
        out.close()
        print("店铺名称", dicts[data], "店铺id", data)
        for page in range(2, 1000):
            print("正在爬取%s页。。。。。" % page)
            a = get_msg(shopid=data, page=page)
            if not a:
                b = input("请按enter键继续，按“1”终止内循环")
                if b == '1':
                    break
            if a ==2:
                break
            time.sleep(random.randint(5, 9))
        #input('程序结束')