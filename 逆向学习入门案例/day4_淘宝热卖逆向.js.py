import  execjs,json
import  time,re
from urllib.parse import quote
from requests_html import HTMLSession
session = HTMLSession()

class TbSpider:
    def __init__(self):
        self.url='https://h5api.m.taobao.com/h5/mtop.alimama.abyss.unionpage.get/1.0/'
        self.headers={
            'Cookie': "t=525a9c902b575a309047f41a1604c979; cna=7NqBHkTAy2ACAXQwZsc8lcHu; thw=cn; cookie2=1348c15629658849cf231d020b20122c; _tb_token_=3bba17eedb416; xlly_s=1; mtop_partitioned_detect=1; _m_h5_tk=01a468ca3afaaf25f6d55cef14ef40ff_1719116195861; _m_h5_tk_enc=28961c71ff5c38c628323c3121eb8ff6; _samesite_flag_=true; 3PcFlag=1719108714000; sgcookie=E100fkOVsixuxCHd0ztcFTHs%2Fy9Z2CRA7Kk236YkbwUqsIn5ZpbE1qzkhhYD8l8Be2CcWeTbhDaRcJoPKpYV0wJpR%2F2Qk5N7PA6wYwNz0mX%2FZzo%3D; wk_cookie2=1a14ae292e7e362f61f577798c53c350; wk_unb=UNN8GJ0NiAWUcw%3D%3D; unb=3310889115; uc1=pas=0&cookie14=UoYfqCoutg2Q4g%3D%3D&cookie16=WqG3DMC9UpAPBHGz5QBErFxlCA%3D%3D&existShop=false&cookie21=VT5L2FSpczFp&cookie15=U%2BGCWk%2F75gdr5Q%3D%3D; uc3=nk2=GcAxdWUrlzvZfXIVr6NeRbzq&id2=UNN8GJ0NiAWUcw%3D%3D&vt3=F8dD3i2ucNVcYV%2FLOUM%3D&lg2=UtASsssmOIJ0bQ%3D%3D; csg=f36cf3da; lgc=zhanghaoyu66739481; cancelledSubSites=empty; cookie17=UNN8GJ0NiAWUcw%3D%3D; dnk=zhanghaoyu66739481; skt=be08e0d4c5facf11; existShop=MTcxOTEwODc1Ng%3D%3D; uc4=nk4=0%40GwlAyxkbVg%2BCTds%2Fa0oK1ploHkVUUcEc6qxZe90%3D&id4=0%40UgQ0oIa4oFulSUn8l4Oi9hZs20sC; tracknick=zhanghaoyu66739481; _cc_=UtASsssmfA%3D%3D; _l_g_=Ug%3D%3D; sg=154; _nk_=zhanghaoyu66739481; cookie1=UtACJtTgS4UliGGIB%2BA3XhSb26u76EZQiWEnG5nrZ7Q%3D; 3pc_partitioned=true; dnk=zhanghaoyu66739481; uc1=pas=0&cookie14=UoYfqCoutg2Q4g%3D%3D&cookie16=WqG3DMC9UpAPBHGz5QBErFxlCA%3D%3D&existShop=false&cookie21=VT5L2FSpczFp&cookie15=U%2BGCWk%2F75gdr5Q%3D%3D; tracknick=zhanghaoyu66739481; lid=zhanghaoyu66739481; _l_g_=Ug%3D%3D; unb=3310889115; lgc=; cookie1=UtACJtTgS4UliGGIB%2BA3XhSb26u76EZQiWEnG5nrZ7Q%3D; login=true; wk_cookie2=1a14ae292e7e362f61f577798c53c350; cookie17=UNN8GJ0NiAWUcw%3D%3D; cookie2=1348c15629658849cf231d020b20122c; _nk_=zhanghaoyu66739481; sgcookie=E100fkOVsixuxCHd0ztcFTHs%2Fy9Z2CRA7Kk236YkbwUqsIn5ZpbE1qzkhhYD8l8Be2CcWeTbhDaRcJoPKpYV0wJpR%2F2Qk5N7PA6wYwNz0mX%2FZzo%3D; cancelledSubSites=empty; sg=154; t=525a9c902b575a309047f41a1604c979; csg=f36cf3da; sn=; _tb_token_=3bba17eedb416; wk_unb=UNN8GJ0NiAWUcw%3D%3D; x5sec=7b22733b32223a2234386661393161363339396461373266222c22617365727665723b33223a22307c434b796233724d47454f6548724b482b2f2f2f2f2f77456144444d7a4d5441344f446b784d5455374d54446671614b4242673d3d227d; tfstk=fuDmMb62hz_QJyj9oY2X1At-Utd8hZw_-VBTWRUwazz5MRdjXlcoAV4vfIwxZP0rrrWvcm3ubVmsMnN9lGjjE2XOHEOjbO2TQeLpppnfcRwwJzJCUIzbf0zNvMyyNmw_QUIRQBpnc2mQZLR0Q32zjl64QPW2q7rLztrN3l7yqlaz7Rz478JzXlbVQOWwu2Wa-AkSUEcY-sGA8wku0FaEmzq7VYq0iyPzrOo-EoV08mkfUZfbjXk3G28RMrln62qKkLWm-mumTWkVzU2s2X0gxx-FtP0j4xFr3hCQVRGqT-kM-Zo7tYkYhbYhpylSbAVrcefQ2foKHf0vPOzxt0uu9YQRp8kmoxPuLgkPa6-n9OZyXY511Sr7qy1LcYujSVA463xlOIN4VoLpq3f1DSr7qyKkq6zuguZvJ; isg=BLGxbRGoczeyedyu75o9ka1-wDtLniUQpP-irJPGrXiXutEM2-414F_c3E7ccr1I",
            'Referer':'https://uland.taobao.com/',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        }
        self.user_input = input("请输入要搜索的商品：")
    def parse_start_url(self):
        time_temp = str(int(time.time()*1000))
        data= {"biz":"sem_single_pc","query":"{\"keyword\":\""+self.user_input+"\",\"pid\":\"430673_1006\",\"sbid\":\"pcrm\",\"refpid\":\"mm_26632258_3504122_32538762\",\"clk1\":\"front_lxqyxp43cb5ekgktj8e\",\"page\":0,\"count\":60,\"offset\":0}","feature":"predict_desc,promotion_price","spm":"a2e0b.20350158.31919782","app_pvid":"201_33.7.59.163_975378_1719112062785","ctm":"spm-url:a2e0b.20350158.search.1;page_url:https%3A%2F%2Fuland.taobao.com%2Fsem%2Ftbsearch%3Frefpid%3Dmm_26632258_3504122_32538762%26keyword%3D%25E8%25AE%25A1%25E7%25AE%2597%25E6%259C%25BA%26clk1%3Db4a02bbf4a994b6a203e2fa2572c0d6a%26upsId%3Db4a02bbf4a994b6a203e2fa2572c0d6a%26spm%3Da2e0b.20350158.search.1%26pid%3Dmm_26632258_3504122_32538762%26union_lens%3Drecoveryid%253A201_33.50.244.104_967635_1719108713802%253Bprepvid%253A201_33.44.179.150_972274_1719112058755"}


        params = f'?jsv=2.5.1&appKey=12574478&t={time_temp}&sign={self.parse_sign(time_temp,data)}&api=mtop.alimama.abyss.unionpage.get&v=1.0&AntiCreep=true&timeout=20000&AntiFlood=true&type=jsonp&dataType=jsonp&callback=mtopjsonp2&data='
        #data进行url转吗
        quote_str = quote(f"{data}")
        print(quote_str)
        url = self.url+params+quote_str
        print(url)
        response =session.get(url,headers=self.headers).content.decode()
        print(response)
        pass
    def parse_sign(self,time_temp,data):
        #正则获取token
        token =re.findall('_m_h5_tk=(.*?)_',self.headers['Cookie'])[0]
        print(token)
        with open('taobao_remai.js', 'r') as f:
            ctx = execjs.compile(f.read())
        str_params=token + "&" + time_temp + "&" + '12574478' + "&" + f'{data}'
        sign = ctx.call('h', str_params)
        print(sign)
        return sign
if __name__ == '__main__':
    tb = TbSpider()
    tb.parse_start_url()