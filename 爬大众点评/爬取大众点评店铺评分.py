import re
import time
import requests
from lxml import etree
from fake_useragent import UserAgent


class DianPing:
    def __init__(self):
        self.url = "http://www.dianping.com/wuhan/ch10"
        self.ua = UserAgent()
        self.headers = {
            "Cookie": "fspop=test; cy=3; cye=hangzhou; _lxsdk_cuid=1753bb608fbc8-0be3842885820b-6b111b7e-1fa400-1753bb608fcc8; _lxsdk=1753bb608fbc8-0be3842885820b-6b111b7e-1fa400-1753bb608fcc8; _hc.v=8429fd3f-f5ca-d6a9-fe0f-58cf71ca55b9.1603024588; s_ViewType=10; ua=%E5%8B%BF%E5%BF%98%E5%BF%83%E5%AE%89_9104; ctu=7fc965fa839279cab50ca6c42a998102e40f1aa3353081dc3b314009932e84da; _lx_utm=utm_source%3Dwww.sogou%26utm_medium%3Dorganic; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1603068428,1603068428,1603106884,1603170526; dper=90107b0184074ada7c44ba1966b4267a693d9ddfa1c6c22c63a356d7867104d7e515d8fdb7c12aaaeb2ba9a633b976e9f7aaef6f6635d21c1e16f94ac3e6d6e12b9871d2bd6e5282ab705ba27b1bd24fc8feec6dab1e6054338442a59a75f64c; ll=7fd06e815b796be3df069dec7836c3df; uamo=13247877023; dplet=b5ab943bc5441bd98e902a41eba0d2d2; _lxsdk_s=175455d29c8-4cb-ce2-446%7C%7C64; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1603187346",
            "User-Agent": self.ua.random  # 获取随机的User-Agent
        }
        self.dic = {}  # class-digit字典

    def get_page(self):
        res = requests.get(self.url, headers=self.headers)
        s = etree.HTML(res.text)
        title_list = s.xpath('//*[@id="shop-all-list"]/ul/li/div[2]/div[1]/a[1]/@title')  # 标题
        dish_list = []  # 招牌菜
        if len(title_list):
            self.get_dict(res.text)
            for i in range(len(title_list)):
                dish_list.append(s.xpath('//*[@id="shop-all-list"]/ul/li[{}]/div[2]/div[4]/a/text()'.format(i + 1))[0])
            score1_list = self.get_score(res.text, len(title_list), 1)  # 口味评分
            score2_list = self.get_score(res.text, len(title_list), 2)  # 环境评分
            score3_list = self.get_score(res.text, len(title_list), 3)  # 服务评分
            for i in range(len(title_list)):
                info = {
                    "店名": title_list[i],
                    "口味评分": score1_list[i],
                    "环境评分": score2_list[i],
                    "服务评分": score3_list[i],
                    "招牌菜": dish_list[i]
                }
                print(info)
        else:
            print("Error！")

    def get_dict(self, html):
        # 提取css文件的url
        css_url = "http:" + re.search('(//.+svgtextcss.+\.css)', html).group()
        print(css_url)
        css_res = requests.get(css_url)
        # 这一步得到的列表内容为css中class的名字及其对应的偏移量
        css_list = re.findall('(un\w+){background:(.+)px (.+)px;', '\n'.join(css_res.text.split('}')))
        # 过滤掉匹配错误的内容，并对y方向上的偏移量初步处理
        css_list = [[i[0], i[1], abs(float(i[2]))] for i in css_list if len(i[0]) == 5]
        # y_list表示在y方向上的偏移量，完成排序和去重
        y_list = [i[2] for i in css_list]
        y_list = sorted(list(set(y_list)))
        # 生成一个字典
        y_dict = {y_list[i]: i for i in range(len(y_list))}
        # 提取svg图片的url
        svg_url = "http:" + re.findall('class\^="un".+(//.+svgtextcss.+\.svg)', '\n'.join(css_res.text.split('}')))[0]
        svg_res = requests.get(svg_url)
        # 得到svg图片中的所有数字
        digits_list = re.findall('>(\d+)<', svg_res.text)
        for i in css_list:
            # index表示x方向上的索引(最小的索引值是0)
            index = int((float(i[1]) + 7) / -12)
            self.dic[i[0]] = digits_list[y_dict[i[2]]][index]

    def get_score(self, html, l, x):
        """
        :param html: 网页源码
        :param l: 迭代长度
        :param x: 1或2或3
        :return: 评分列表
        """
        s = etree.HTML(html)
        num_list = []
        for i in range(l):
            t = s.xpath('//*[@id="shop-all-list"]/ul/li[{}]/div[2]/span/span[{}]/b/text()'.format(i + 1, x))[0]
            c = s.xpath('//*[@id="shop-all-list"]/ul/li[{}]/div[2]/span/span[{}]/b/span/@class'.format(i + 1, x))
            num = self.dic[c[0]] + '.' + self.dic[c[1]] if t == '.' else self.dic[c[0]] + '.1'
            num_list.append(num)
        return num_list


if __name__ == '__main__':
    dp = DianPing()
    dp.get_page()