"""
解析菜馆信息
"""
import requests
import re
import json


class ParseRestaurantInfo(object):
    target_url = 'https://www.meituan.com/meishi/{p_id}/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3754.400 QQBrowser/10.5.4020.400',
    }

    def __init__(self, restaurant_id):
        self.restaurant_id = restaurant_id

        self.go_to_restaurant()

    def go_to_restaurant(self):
        """执行访问
        """
        url = self.target_url.format(p_id=self.restaurant_id)
        data = requests.get(url, headers=self.headers).text
        print(data)
        # 提取有效区域
        data = re.search(r'12315消费争议(.*?)"dealList":', data, flags=re.DOTALL)

        if data:
            self.parse_html(data.group(1))
        else:
            yanzhengurl = 'https://verify.meituan.com/v2/captcha?request_code=bd983054a81f4d5ba392e13cf183c3d4&action=spiderindefence&randomId=0.43945441023651055'
            'https://verify.meituan.com/v2/captcha?request_code=f3e8396c5e1e47d793a916a3ddf4431a&action=spiderindefence&randomId=0.5488311310535803'
            'https://verify.meituan.com/v2/captcha?request_code=8d474364381941f6bd4025857ed09a03&action=spiderindefence&randomId=0.4945929465218366'
            print('访问失效')

    @staticmethod
    def parse_html(data):
        """解析数据
        """

        # 细节信息
        detail_info = re.search(
            r'"detailInfo":\{"poiId":(\d+),"name":"(.*?)","avgScore":(.*?),"address":"(.*?)","phone":"(.*?)","openTime":"(.*?)","extraInfos":\[(.*?)\],"hasFoodSafeInfo":(.*?),"longitude":(.*?),"latitude":(.*?),"avgPrice":(\d+),"brandId":(\d+),"brandName":"(.*?)",".*?photos":{"frontImgUrl":"(.*?)","albumImgUrls":(.*?)},"recommended":(.*?),"crumbNav":(.*?),"prefer',
            data)
        if detail_info:
            poiId = detail_info.group(1)
            name = detail_info.group(2)
            avgScore = detail_info.group(3)
            address = detail_info.group(4)
            phone = detail_info.group(5)
            openTime = detail_info.group(6)
            extraInfos = detail_info.group(7)
            hasFoodSafeInfo = detail_info.group(8)
            longitude = detail_info.group(9)
            latitude = detail_info.group(10)
            avgPrice = detail_info.group(11)
            brandId = detail_info.group(12)
            brandName = detail_info.group(13)
            frontImgUrl = detail_info.group(14)
            albumImgUrls = detail_info.group(15)

            # 其他信息解析
            if extraInfos:
                items = json.loads("[" + extraInfos + "]")
                extraInfos = ''
                for item in items:
                    extraInfos = item.get('text') + '  ' + extraInfos
            # 推荐菜处理
            recommended = json.loads(detail_info.group(16))

            # 面包屑抽离
            crumbNav = json.loads(detail_info.group(17))
            area = crumbNav[0].get('title')[:-2]
            food_type = crumbNav[2].get('title')[len(area):]
            print('区域: ', area, ' 餐饮类型: ', food_type)

            print_str = """
========解析结果========
店铺ID: {poiId}
餐馆名称: {name}
综合评分: {avgScore}
详细地址: {address}
联系电话: {phone}
营业时间: {openTime}
其他信息: {extraInfos}
是否有卫生许可证: {hasFoodSafeInfo}
经度: {longitude}
纬度: {latitude}
平均消费: {avgPrice}
所属品牌ID: {brandId}
品牌: {brandName}
店铺主图: {frontImgUrl}
相册: {albumImgUrls}
推荐菜品区：""".format(poiId=poiId, name=name, avgScore=avgScore, address=address, phone=phone, openTime=openTime,
                 extraInfos=extraInfos, hasFoodSafeInfo=hasFoodSafeInfo, longitude=longitude, latitude=latitude,
                 avgPrice=avgPrice, brandId=brandId, brandName=brandName, frontImgUrl=frontImgUrl,
                 albumImgUrls=albumImgUrls)

            print(print_str)

            # 打印推荐菜
            for item in list(recommended):
                # recommend_id = item['id']  # 推荐菜id
                recommend_name = item['name']  # 推荐菜名
                recommend_price = item['price']  # 菜品价格
                recommend_img = item['frontImgUrl']  # 菜品图片
                print(recommend_name, end=' ')

        else:
            print('数据信息失败')


if __name__ == '__main__':
    p_id = input('请输入餐馆id')
    # p_id = '364942'
    # p_id = '98327266'
    # p_id = '6902945'
    ParseRestaurantInfo(p_id)