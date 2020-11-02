from __future__ import print_function
import base64,requests,csv,time
from urllib.parse import quote
from urllib.parse import unquote

from PIL import Image
import zlib
def decode_token(token):
    # base64解码
    token_decode = base64.b64decode(token)
    #print(token_decode)
    # 二进制解压
    token_string = zlib.decompress(token_decode)
    print(token_string)

token = 'eJxtj1uPokAQhf9Lv0qku7n7BiMuN3VEwF0n88ClEUERoRGGzf736UnGl8kmlZxTVV9Oqv6C1s7AAkGoQciBB2nBAqA5nMuAA7RjG0lDCpZkJMuIAemPmYw4kLTREizeVEnkVCS9fw181r9hKKocQhJ+554eMY9FVl+UzSBQUNp0C55PyvmVnGkf1/P0duWZ74oz39SYZ4c8oWEY/kchWVJUUdEEHrDca8BymVbfGn8rffZr9iIL7c6nmjniDJcpRNth0ncGeVGy7SqTadGYolcZ5ObeD56lxwlqHLjn8Un1e3ureJXpzHQ11dXu4KGHmgfEKMoCJpTUoTVYH/4jGJc7Phn53NI0t1JHu9D2ZW6fhjsuw+KPS/2PvY8z+XI89StHk7KI+L+3MnqlGOthdR+3UDIylLZ3f6Kr5tK7L5MXlXG73ODIqlYH37aOox+QoD67srJxElOMdo9Znh1dof+1vom5hnRBOZILHjRDWJsz3AkkuIapOsVxvmk1mJpVAv59AiJYmoQ='
#ddd = decode_token(token)

# sign="eJwlzU1OwzAQBeC7dOFd6thpE4LkBeoKqWLHAab1pJ0S/2g8RuIO7LkEJ+A8cA8sWL1v8fTeBhjh0btenUHwHyRvTxDQ/bx/fH99Kk8xIh9SjfIgwq2jUhYKtRySR2d6lZguFJ95dVeRXO61Pt22AUkqxO05Bd1crqRztFpluKCzLVjarDN2VHkFWRIHZxRTeTniK67NJbE4VQv+fdZK3uGMo4f91A37Zel2w9B3ME+2s3eTmUc8zaafNr90cEkb"
# fff = decode_token(sign)
# url = 'eJxtT11vgkAQ/C/3KhGO8nGY+ACo5awFBPxA0wdAPBAOFFCiTf97r0l9aNJkk5mdndnsfoIGH8AICoImCBy4pQ0YATgUhgrgQNeyiaxBhFhJigo5kPzVVJFpcbOegNEeyRKHoPzxI3is34uChDgIZfGDe3LIuCix+nFhZgJZ151HPB+fhjTNu2tUDZOa8oy3Wc6zG/6fA5anAcszLH4x+sXu2b+zV9iGNicVY+m8L0/x1O5P+tLbpllipD62dFyQbpqFQf3qmHjyyLGaZsij2ErPO6JfI8ONTTIotGPAD1xiWBtY+hcdTfnCvouSbSC15l8UpWjTcIDMtlqsav9RI0zk2TwxwittSo8458Ux2WgObp184R6rduX4hqUmxvpAT3lygcuJpToHcmf+ihKomabVm+o2cF/vvX8T6cYm7/55xtti6dm70A1dp7/MaoWWh8BaxzMfRm+W/1DF/hGtmxXSplt9J+N5Px6Dr2/3tJFV'
#
# print(quote(url, 'utf-8'))
# text = 'https://verify.meituan.com/v2/web/general_page?action=spiderindefence&requestCode=06aad59d202048f49b47af17ced9fed0&platform=1000&adaptor=auto&succCallbackUrl=https%3A%2F%2Foptimus-mtsi.meituan.com%2Foptimus%2FverifyResult%3ForiginUrl%3Dhttp%253A%252F%252Fbj.meituan.com%252Fmeishi%252F310689'
# print(unquote(text, 'utf-8'))

# r_img = requests.get(image_src,headers=headers)
# with open('code.png','wb') as fp:
#     fp.write(r_img.content)
#     code = input('请输入验证码：')
# filename = './店铺信息测试.csv'
# datas = []
# with open(filename,'r',encoding='utf-8') as csvfile:
#     csv_reader = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的文件
#     #header = next(csv_reader)        # 读取第一行每一列的标题
#     for rows in csv_reader:
#         print(rows[5])
timestamp = 1595564735

#转换成localtime
time_local = time.localtime(timestamp)
#转换成新的时间格式(2016-05-05 20:28:54)
dt = time.strftime("%Y-%m-%d %H:%M:%S ",time_local)

print(dt)


response = requests.get(url ='https://verify.meituan.com/v2/captcha?request_code=4d82cfcfc5fd469baa2821f139eda4a7&action=spiderindefence&randomId=0.004648075305734967')
#print(response.text)
# 1.打开图片
# im = Image.open()
# print(im)
#
# # 2.查看图片文件内容
# print("图片文件格式：" + im.format)
# print("图片大小：" + str(im.size))
# print("图片模式：" + im.mode)
#
# # 3.显示当前图片对象
# im.show()

import re  # 用于正则
from PIL import Image  # 用于打开图片和对图片处理
import pytesseract  # 用于图片转文字
from selenium import webdriver  # 用于打开网站
import time  # 代码运行停顿


# class VerificationCode:
#     def __init__(self):
#         self.driver = webdriver.Firefox()
#         self.find_element = self.driver.find_element_by_css_selector
#
#     def get_pictures(self):
#         self.driver.get('https://verify.meituan.com/v2/web/general_page?action=spiderindefence&requestCode=7ebef3bc84e4445095e41c978fc67444&platform=1&adaptor=auto&succCallbackUrl=https%3A%2F%2Foptimus-mtsi.meituan.com%2Foptimus%2FverifyResult%3ForiginUrl%3Dhttps%253A%252F%252Fwww.meituan.com%252Fmeishi%252F61998%252F')  # 打开登陆页面
#         self.driver.save_screenshot('pictures.png')  # 全屏截图
#         page_snap_obj = Image.open('pictures.png')
#         img = self.find_element('#pic')  # 验证码元素位置
#         time.sleep(1)
#         location = img.location
#         size = img.size  # 获取验证码的大小参数
#         left = location['x']
#         top = location['y']
#         right = left + size['width']
#         bottom = top + size['height']
#         image_obj = page_snap_obj.crop((left, top, right, bottom))  # 按照验证码的长宽，切割验证码
#         image_obj.show()  # 打开切割后的完整验证码
#         self.driver.close()  # 处理完验证码后关闭浏览器
#         return image_obj
#
#     def processing_image(self):
#         image_obj = self.get_pictures()  # 获取验证码
#         img = image_obj.convert("L")  # 转灰度
#         pixdata = img.load()
#         w, h = img.size
#         threshold = 160
#         # 遍历所有像素，大于阈值的为黑色
#         for y in range(h):
#             for x in range(w):
#                 if pixdata[x, y] < threshold:
#                     pixdata[x, y] = 0
#                 else:
#                     pixdata[x, y] = 255
#         return img
#
#     def delete_spot(self):
#         images = self.processing_image()
#         data = images.getdata()
#         w, h = images.size
#         black_point = 0
#         for x in range(1, w - 1):
#             for y in range(1, h - 1):
#                 mid_pixel = data[w * y + x]  # 中央像素点像素值
#                 if mid_pixel < 50:  # 找出上下左右四个方向像素点像素值
#                     top_pixel = data[w * (y - 1) + x]
#                     left_pixel = data[w * y + (x - 1)]
#                     down_pixel = data[w * (y + 1) + x]
#                     right_pixel = data[w * y + (x + 1)]
#                     # 判断上下左右的黑色像素点总个数
#                     if top_pixel < 10:
#                         black_point += 1
#                     if left_pixel < 10:
#                         black_point += 1
#                     if down_pixel < 10:
#                         black_point += 1
#                     if right_pixel < 10:
#                         black_point += 1
#                     if black_point < 1:
#                         images.putpixel((x, y), 255)
#                     black_point = 0
#         # images.show()
#         return images
#
#     def image_str(self):
#         image = self.delete_spot()
#         pytesseract.pytesseract.tesseract_cmd = r"c:\programdata\anaconda3\lib\site-packages\tesseract.exe"  # 设置pyteseract路径
#         result = pytesseract.image_to_string(image)  # 图片转文字
#         resultj = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "", result)  # 去除识别出来的特殊字符
#         result_four = resultj[0:4]  # 只获取前4个字符
#         # print(resultj)  # 打印识别的验证码
#         return result_four
#
#
# if __name__ == '__main__':
#     a = VerificationCode()
#     a.image_str()