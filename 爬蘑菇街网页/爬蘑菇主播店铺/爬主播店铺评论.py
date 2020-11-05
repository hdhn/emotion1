import requests
import time,csv,random,json
headers = {
    'cookie': '__mgjuuid=f1672d9a-25bc-4835-85d0-1a39654cb591; _ga=GA1.2.919819752.1601260014; FRMS_FINGERPRINTN=xNK728q1RCOo03XT7kkXRg; _mwp_h5_token_enc=06623668ef97650b3ddc323368e7a479; _mwp_h5_token=0aaeea9d396ee7ea6ac2cd5e3ffcb94b_1602120056450; _gid=GA1.2.204211445.1602231174',
    'referer': 'https://pc.mogu.com/content/personal/11no1nk?&acm=3.ms.1_9_11no1nk.453.88102-68998.7Er9Msd9QPLQt.sd_117-swt_453-imt_21-t_7Er9Msd9QPLQt-pit_53-qid_579083-dit_-idx_0-dm1_5001&ptp=31.WHb0z.0.0.fIcLIb9u',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3775.400 QQBrowser/10.6.4209.400'
}
url1 = 'https://api.mogu.com/h5/mwp.darling.feedList/1/?data={"pageSize":20,"mbook":"eyJwYWdlIjoxLCJ0IjoidUV1TlVzZDlTOUpxMCIsImZlZWRzT2ZVc2VyUGFnZSI6MTYwMTQ0ODQzNywidXNlckZlZWRTdGF0dXMiOjB9","uid":"11no1nk","stickyId":"","page":2,"clientType":"pc"}&mw-appkey=100028&mw-ttid=NMMain%40mgj_pc_1.0&mw-t=1602462218404&mw-uuid=f1672d9a-25bc-4835-85d0-1a39654cb591&mw-h5-os=unknown&mw-sign=786ad5ed0c891e74f1f847ffb4c5c4b7&callback=mwpCb6'
for p in range(1,20):
    response = requests.get(url = url1,headers = headers)
    print(response.text)
    # htmls = json.loads(response.text[7:-1])['data']['list']
    # for html in htmls:
    #     item = html['data']
    #     print(json.loads(item)['feedId'])
    #     break
    time.sleep(3)