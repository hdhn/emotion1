from bs4 import BeautifulSoup
import re
from fake_useragent import UserAgent  #随机生成User-Agent
import time
import random

class DZDP_Comment():
    def __init__(self,shop_num):  #传入商铺的num即可下载评论
        self.headers={
    'User-Agent':UserAgent().random,
    'Cookie':'fspop=test; cy=3; cye=hangzhou; _lxsdk_cuid=1753bb608fbc8-0be3842885820b-6b111b7e-1fa400-1753bb608fcc8; _lxsdk=1753bb608fbc8-0be3842885820b-6b111b7e-1fa400-1753bb608fcc8; _hc.v=8429fd3f-f5ca-d6a9-fe0f-58cf71ca55b9.1603024588; s_ViewType=10; ua=%E5%8B%BF%E5%BF%98%E5%BF%83%E5%AE%89_9104; ctu=7fc965fa839279cab50ca6c42a998102e40f1aa3353081dc3b314009932e84da; _lx_utm=utm_source%3Dwww.sogou%26utm_medium%3Dorganic; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1603024587,1603068428,1603068428,1603106884; dper=90107b0184074ada7c44ba1966b4267abffca5d03a1590ad10afb48da378aece79c47109e7d2666f04958526a866332405eed03572a376a66c490c6df52f6384a18dc617fb897664fcb340ab8ed2d9815a77deeb611bd0f7ef2ac61c2bdbe6ed; ll=7fd06e815b796be3df069dec7836c3df; uamo=13247877023; dplet=634f02b9ed59fd623d98e05bcb818739; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1603111403; _lxsdk_s=17540c2447c-57b-404-a69%7C%7C268',
    'Referer':'http://www.dianping.com/shop/l8uNm5kgLP4n6eLq/review_all',
    'Connection':'keep-alive',
}
        self.start_url='http://www.dianping.com/shop/{}/review_all'.format(shop_num)  #评论首页
        self.font_size=14
        self.start_y=23

    def get_page(self,url):
        from urllib import request
        from http import cookiejar
        # 声明一个CookieJar对象实例来保存cookie
        cookie = cookiejar.CookieJar()
        # 利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
        cookie_support = request.HTTPCookieProcessor(cookie)
        # 通过CookieHandler创建opener
        opener = request.build_opener(cookie_support)
        # 创建Request对象
        req = request.Request(url, headers=self.headers)
        response = opener.open(req)
        html = response.read().decode('utf-8')
        return html

    def get_font_dict_by_offset(self,url):  #获取坐标偏移的文字字典, 会有最少两种形式的svg文件（目前只遇到两种）
        html=self.get_page(url)
        font_dict = {}
        y_list = re.findall(r'd="M0 (\d+?) ', html)
        if y_list:
            font_list = re.findall(r'<textPath .*?>(.*?)<', html)
            for i, string in enumerate(font_list):
                y_offset = self.start_y - int(y_list[i])
                sub_font_dict = {}
                for j, font in enumerate(string):
                    x_offset = -j * self.font_size
                    sub_font_dict[x_offset] = font
                font_dict[y_offset] = sub_font_dict
        else:
            font_list = re.findall(r'<text.*?y="(.*?)">(.*?)<', html)
            for y, string in font_list:
                y_offset = self.start_y - int(y)
                sub_font_dict = {}
                for j, font in enumerate(string):
                    x_offset = -j * self.font_size
                    sub_font_dict[x_offset] = font
                font_dict[y_offset] = sub_font_dict
        return font_dict

    def get_font_dict(self):  #找到隐藏字的映射关系                     #构建隐藏文字与位置元素数值对应的映射关系：
        #1、根据首页获得css样式
        html=self.get_page(self.start_url)
        css= re.findall(r'<link re.*?css.*?href="(.*?svgtextcss.*?)">', html)
        css_link='http:'+css[0]   #获得css_link
        #print(css_link)
        #2、根据css样式获得对应的字典
        html=self.get_page(css_link)
        background_image_link = re.findall(r'background-image:.*?\((.*?svg)\)', html)
        background_image_link='http:'+background_image_link[2]#一共有3个background_image_link，但是第一个的链接不是映射关系，第二个的映射关系很少【并且实验证明有问题】，所以选择第三个映射关系
        html=re.sub(r'span.*?\}','',html)
        group_offset_list = re.findall(r'\.([a-zA-Z0-9]{5,6}).*?round:(.*?)px (.*?)px;', html)
        #print(group_offset_list)
        font_dict_by_offset=self.get_font_dict_by_offset(background_image_link)
        #print(font_dict_by_offset)
        font_dict={}
        for class_name,x_offset,y_offset in group_offset_list:
            x_offset=x_offset.replace('.0','')
            y_offset=y_offset.replace('.0','')
            try:
                font_dict[class_name]=font_dict_by_offset[int(y_offset)][int(x_offset)]
            except:
                font_dict[class_name]=''
        return font_dict

    def get_num(self):
        html=self.get_page(self.start_url)
        soup=BeautifulSoup(html,'html.parser')
        pages=soup.find_all('div',{'class':{'reviews-pages'}})[0]
        num=int(pages('a')[-2].text.strip())
        return num

    def get_comment(self,url,font_dict):
        html=self.get_page(url)
        class_set=set() #定义一个空集合  【不允许重复】
        for span in re.findall(r'<span class="([a-zA-Z0-9]{5,6})"></span>', html):
            class_set.add(span)
        for class_name in class_set:
            try:
                html=re.sub('<span class="{}"></span>'.format(class_name),font_dict[class_name],html)
            except:
                html=re.sub('<span class="{}"></span>'.format(class_name),'',html)
        soup=BeautifulSoup(html,'html.parser')
        divs=soup.find_all('div',{'class':{'review-words'}})
        for div in divs:
            comment=div.text.strip().replace('收起评论','').replace('\n','').replace('\t','').replace(' ','')
            with open ('comment.txt','a',encoding='utf-8')as f:
                f.write(comment+'\n')

    def main(self): #传入商家店铺代码
        font_dict=self.get_font_dict()
        num = self.get_num()
        print('共{}页评论'.format(num))
        for i in range(1,num+1):
            print('正在爬取第{}页评论'.format(i))
            url=self.start_url+'/p{}'.format(i)
            self.get_comment(url,font_dict)
            time.sleep(random.randint(1,3))  #每次访问完一页，休息个十几秒   【怕被反爬虫】

fp_comment=DZDP_Comment('l8uNm5kgLP4n6eLq')  #喵の鍋日式小火锅
fp_comment.main()