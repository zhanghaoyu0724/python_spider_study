
"""
js逆向查找 js位置的方法：


"""
import time
from datetime import datetime

#

#import  js2py
# #创建js 环境
# js = js2py.EvalJs()
# with open('1.js','r') as f:
#     data=f.read()
# js.execute(data)
#
# print(js.parse('张浩宇'))

import  execjs,json
#
# with open('1.js','r') as f:
#     ctx = execjs.compile(f.read())
# sign =ctx.call('parse','张浩宇')
# print(sign)

from requests_html import HTMLSession

session = HTMLSession()


class BdSpider:
    def __init__(self):
        self.user_input = input("请输入想翻译的文字")
        self.url = 'https://fanyi.baidu.com/v2transapi'
        self.langdetect_url ='https://fanyi.baidu.com/langdetect'
        self.headers ={
            'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie':'PSTM=1699141691; BIDUPSID=D3E5010C72D5026CDEF68D8390D61DBD; BDUSS=5PbHhOUkpydFBNYVpEa1JNT2tCV1FrZmlwRmp4Qlh0dXRlZmYycmtVamdhd0ZtSVFBQUFBJCQAAAAAAAAAAAEAAABqCYSuwLbM7HZ2MTEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAODe2WXg3tllU3; BDUSS_BFESS=5PbHhOUkpydFBNYVpEa1JNT2tCV1FrZmlwRmp4Qlh0dXRlZmYycmtVamdhd0ZtSVFBQUFBJCQAAAAAAAAAAAEAAABqCYSuwLbM7HZ2MTEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAODe2WXg3tllU3; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BAIDUID=892AF54F1D080A8A3ACFA419AF395611:SL=0:NR=10:FG=1; H_PS_PSSID=60236_60297_60325_60336_60333_60346_60376; H_WISE_SIDS=60236_60297_60325_60336_60333_60346_60376; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_WISE_SIDS_BFESS=60236_60297_60325_60336_60333_60346_60376; BA_HECTOR=058121a48l212ga421ag8g2h0e9uin1j7delt1u; BAIDUID_BFESS=892AF54F1D080A8A3ACFA419AF395611:SL=0:NR=10:FG=1; ZFY=uwYMDy6DjO7l8:BytkkUEHkCLHF:Aj0fW:AweAeK:BQO4xg:C; delPer=0; PSINO=5; Hm_lvt_246a5e7d3670cfba258184e42d902b31=1719060362; Hm_lpvt_246a5e7d3670cfba258184e42d902b31=1719060362; smallFlowVersion=old; RT="z=1&dm=baidu.com&si=afbedf85-49bc-405a-a98f-63df47b273ee&ss=lxq45bxs&sl=7&tt=6en&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=1uy8&ul=2zot&hd=2ztw"; APPGUIDE_10_7_1=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1719060492; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1719060568; ab_sr=1.0.1_NmE5YjBjNzBmMzQwZThjODdmMGFhZDM2MjY4OTFmNDdjNmQyODI3ZmUxODc5MjQ5ZmRiNjUwZTEyYTU1MTQ0ZmYxOGM3MGRiNDk0NjViNzc1YWViZDI4NTI2ZWQ3ZmViZDUxMjJmYmE4MjE4MWY5ZDhkYjI4NTMzNzFjN2M5MzNlZWUwMjM5MjZkYWU1Yjg3MTk5NTJkOGZiYmQzMDY4N2U3NDlhMTNjYWJkZTViNTNlODg0NmFmMGVmNGM5NWE1',
            'Host':'fanyi.baidu.com',
            'Origin':'https://fanyi.baidu.com',
            'Referer':'https://fanyi.baidu.com/',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
        }
    def pares_input_type(self):
        data={
            'query' :self.user_input
        }
        response = session.post(url=self.langdetect_url, headers=self.headers,data=data).json()
        return response['len']

    def pares_input_content(self):
        data={
            'from': 'zh',
            'to': 'en',
            'query': self.user_input,
            'simple_means_flag': 3,
            'sign': self.pares_sign(),
            'token': 'bb1692102665864c1c7e9368b0e1526b',
            'domain': 'common'
        }
        response =session.post(url=self.url, headers=self.headers,data=data).json()
        print(response['trans_result']['data'][0]['dst'])

    def pares_sign(self):
        with open('1.js', 'r') as f:
            ctx = execjs.compile(f.read())
        sign =ctx.call('parse',self.user_input)
        return sign

if __name__ == '__main__':
    print(time.time())
    spider = BdSpider()
    spider.pares_input_content()