import json, zlib, base64, time


class MakeToken():
    """
    测试2019-4-21日可用
    仅作为学术交流！如有侵权，联系作者删除
    美团【餐馆列表】Token生成
    """

    def __init__(self, areaId, cityName, originUrl, page):
        self.areaId = areaId
        self.cityName = cityName
        self.originUrl = originUrl
        self.page = page
        self.uuid = 'd65acdaf-7141-4690-9eda-67bcd7279e68'  # Demo c6eada3ffd8e444491e9.1555472928.3.0.0

    def join_sign(self):
        # 参数
        sign = 'areaId={areaId}&cateId=0&cityName={cityName}&dinnerCountAttrId=&optimusCode=10&originUrl={originUrl}&page={page}&partner=126&platform=1&riskLevel=1&sort=&userId=&uuid={uuid}'
        _str = sign.format(areaId=self.areaId, cityName=self.cityName, originUrl=self.originUrl+'meishi/', page=self.page,
                           uuid=self.uuid)
        sign = base64.b64encode(zlib.compress(bytes(json.dumps(_str, ensure_ascii=False), encoding="utf8")))
        sign = str(sign, encoding="utf8")

        return sign

    @property
    def join_token(self):
        str_json = {}
        str_json['rId'] = 100900
        str_json['ver'] = '1.0.6'
        str_json['ts'] = int(time.time()*1000)
        str_json['cts'] = int(time.time()*1000+50)
        str_json['brVD'] = [854,815]  #[1920, 315]
        str_json['brR'] = [[2048,1152],[2048,1112],24,24] #[[1920, 1080], [1920, 1057], 24, 24]
        str_json['bI'] = [self.originUrl+'meishi/',self.originUrl]
        str_json['mT'] = []
        str_json['kT'] = []
        str_json['aT'] = []
        str_json['tT'] = []
        str_json['aM'] = ''
        str_json['sign'] = self.join_sign()
        token_decode = zlib.compress(
            bytes(json.dumps(str_json, separators=(',', ':'), ensure_ascii=False), encoding="utf8"))
        token = str(base64.b64encode(token_decode), encoding="utf8")
        return token

def decode_token(token):
    # base64解码
    token_decode = base64.b64decode(token)
    #print(token_decode)
    # 二进制解压
    token_string = zlib.decompress(token_decode)
    return token_string

if __name__ == '__main__':
    # 测试数据
    areaId = '0'
    page = '1'
    cityNames = {'北京':'http://bj.meituan.com/',
                 '上海':'http://sh.meituan.com/',
                '深圳':'http://sz.meituan.com/',
                '广州':'http://gz.meituan.com/',
                '杭州':'http://hz.meituan.com/',
                '南京':'http://nj.meituan.com/',
                '成都':'http://cd.meituan.com/',
                '武汉':'http://wh.meituan.com/',
                '苏州':'http://su.meituan.com/',
                '重庆':'http://cq.meituan.com/',
                '天津':'http://tj.meituan.com/',
                '郑州':'http://zz.meituan.com/',
                '西安':'http://xa.meituan.com/',
                '长沙':'http://chs.meituan.com/',
                '宁波':'http://nb.meituan.com/',
                '佛山':'http://fs.meituan.com/',
                '青岛':'http://qd.meituan.com/',
                '合肥':'http://hf.meituan.com/',
                '济南':'http://jn.meituan.com/',
                '东莞':'http://dg.meituan.com/',
                '福州':'http://fz.meituan.com/',
                '无锡':'http://wx.meituan.com/',
                '厦门':'http://xm.meituan.com/',
                '珠海':'http://zh.meituan.com/',
                '昆明':'http://km.meituan.com/'}
    for cityName in cityNames:
        originUrl = cityNames[cityName]
        token = MakeToken(areaId, cityName, originUrl, page)
    # ssss = decode_token(token.join_token)
    # print(ssss)
        print(token.join_token)
        exit()