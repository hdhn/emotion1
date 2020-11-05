import base64,requests,csv
from urllib.parse import quote
from urllib.parse import unquote

import zlib
def decode_token(token):
    # base64解码
    token_decode = base64.b64decode(token)
    #print(token_decode)
    # 二进制解压
    token_string = zlib.decompress(token_decode)
    print(token_string)

token = 'eJxtj1uPokAQhf9Lv0qku7n7BiMuN3VEwF0n88ClEUERoRGGzf736UnGl8kmlZxTVV9Oqv6C1s7AAkGoQciBB2nBAqA5nMuAA7RjG0lDCpZkJMuIAemPmYw4kLTREizeVEnkVCS9fw181r9hKKocQhJ+554eMY9FVl+UzSBQUNp0C55PyvmVnGkf1/P0duWZ74oz39SYZ4c8oWEY/kchWVJUUdEEHrDca8BymVbfGn8rffZr9iIL7c6nmjniDJcpRNth0ncGeVGy7SqTadGYolcZ5ObeD56lxwlqHLjn8Un1e3ureJXpzHQ11dXu4KGHmgfEKMoCJpTUoTVYH/4jGJc7Phn53NI0t1JHu9D2ZW6fhjsuw+KPS/2PvY8z+XI89StHk7KI+L+3MnqlGOthdR+3UDIylLZ3f6Kr5tK7L5MXlXG73ODIqlYH37aOox+QoD67srJxElOMdo9Znh1dof+1vom5hnRBOZILHjRDWJsz3AkkuIapOsVxvmk1mJpVAv59AiJYmoQ='
#token = 'eJx1T8tugkAU%2FZfZSmQGEQZ3WESgWgWR2jRdyBQZkJcwyqPpv3dM7KZJk5ucxz05ufcL1PYnmCEINQgFcItqMANoDMcKEABr%2BGaqSQhBRZkgCQuA%2FPGUqQDCOjDA7B1PZQEj9eNueFy%2FS1DGAkJT6UP45YhzSeZzT9k8BChjVTMTRZaO8yhh12MxJmUuct7QRORH%2FBMAvCH3eQPH8wOPD2S%2Fes2f4RVNEhecRU6bpT67toPueptRElfSiF0OC11nRuZaxsFVWjs99VJiVyuHzAkdFWSDayci9jnwh7VDt%2Fpb17JV5c1jX4wjfzB0FWnipMNit8vqzrLO255QgxamSc2DXaXNMglpE%2BTLsA%2FVoUxwfNQme4ZwSXeuc8oj4zJszScWVHQo983KynYMSTcUH87b0Fi9ZBtcnHQjw23HqwL7pmrV3nvVeiy%2FLNZiRkLoqvmn%2BiwvEo31kYOaq8ag5cXlKTZ7skgr8P0D6sqVOw%3D%3D'
#ddd = decode_token(token)
#
#
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
filename = './店铺信息测试.csv'
datas = []
with open(filename,'r',encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的文件
    #header = next(csv_reader)        # 读取第一行每一列的标题
    for rows in csv_reader:
        print(rows[5])