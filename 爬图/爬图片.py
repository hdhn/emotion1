import requests
import re
import os
import time
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3754.400 QQBrowser/10.5.4020.400'
}
zhuye = requests.get('https://www.vmgirls.com',headers=headers)
hhhh = zhuye.text
url00 = re.findall('<a target="_blank" rel="noopener noreferrer" href="(.*?)">.*?</a>',hhhh)
for liss in url00:
    zhuye1 = response = requests.get(liss,headers=headers)
    html1 =zhuye1.text
    url200 = re.findall('<a href="(.*?)" class="list-title text-md h-2x" title=".*?">.*?</a>',html1)
    for lisss in url200:
        response = requests.get(lisss,headers=headers)
        #print(response.request.headers)
        html = response.text
        """解析网站"""
        #print(html)
        dir_name = re.findall('<h1 class="post-title h3">(.*?)</h1>',html)[0]
        #print(dir_name)
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)
        urls = re.findall('<p><a href="(.*?)" alt=".*?" title=".*?">',html)
        print(urls)
        """保存图片"""
        for url in urls:
            time.sleep(1)
            #图片的名字
            file_name = url.split('/')[-1]
            response = requests.get(url,headers = headers)
            with open(dir_name+'/'+file_name,'wb') as f:
                f.write(response.content)