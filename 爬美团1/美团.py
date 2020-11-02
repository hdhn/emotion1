import requests
import re
import os
import time
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3754.400 QQBrowser/10.5.4020.400',
    'Cookie':'_lx_utm=utm_source%3Dwww.sogou%26utm_medium%3Dorganic; _lxsdk_cuid=17289f6f39f0-0379aadb1ad974-335e4f7a-240000-17289f6f3a0c8; ci=1; rvct=1; _hc.v=3becfc73-dec1-7e6e-5860-26583f0257ef.1591453491; uuid=33a7eb3cb30a4075ac0c.1591472130.1.0.0; _lxsdk=17289f6f39f0-0379aadb1ad974-335e4f7a-240000-17289f6f3a0c8; lat=39.889788; lng=116.65564; client-id=44a0a1e6-0dbc-4da5-be0c-9da04769d841; _lxsdk_s=1728ec9f4ab-b60-503-db2%7C%7C2'
}
zhuye = requests.get('https://zh.meituan.com/meishi/',headers=headers)
hhhh = zhuye.text