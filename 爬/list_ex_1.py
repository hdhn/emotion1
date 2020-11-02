import urllib
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = 'http://py4e-data.dr-chuck.net/comments_834796.html'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')
print(soup)
tags = soup('span')
print(tags)
sum1 = 0
i = 0
for tag in tags:
    # print('TAG:',tag)
    # print('CLASS:',tag.get('href',None))
    print('Contents:',tag.contents[0])
    sum1 += int(tag.contents[0])
    i += 1
print('{i}个数的总和为{sum1}'.format(i=i,sum1=sum1))
    # print('Attrs:',tag.attrs)
