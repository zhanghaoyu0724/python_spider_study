import requests
from urllib.parse import  urlencode

cookies = {
    'Hm_lvt_a65c0ab491f55a0bdb4754d6358a8ae9': '1719731605',
    'Hm_lpvt_a65c0ab491f55a0bdb4754d6358a8ae9': '1719731711',
    'VOLCALB': '14ea67d4d82fb7927e69198e5981c5d9|1719732124|1719731604',
    'VOLCALBCORS': '14ea67d4d82fb7927e69198e5981c5d9|1719732124|1719731604',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    # 'Cookie': 'Hm_lvt_a65c0ab491f55a0bdb4754d6358a8ae9=1719731605; Hm_lpvt_a65c0ab491f55a0bdb4754d6358a8ae9=1719731711; VOLCALB=14ea67d4d82fb7927e69198e5981c5d9|1719732124|1719731604; VOLCALBCORS=14ea67d4d82fb7927e69198e5981c5d9|1719732124|1719731604',
    'Referer': 'https://pbl.neoscholar.com/List?coursePhases=6&coursePhases2=4&nationality=33',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}

data ={
    'standardCode': 'P0121,P0122,P0124,P0130,P0132',
    'xids': '2',
    'xid2s': '11',
    'coursePhases': '2',
    'coursePhases2': '4',
    'nationality': '33',
    'courseCity': '',
    'name': '',
    'url': 'https://pbl.neoscholar.com/List?coursePhases=6&coursePhases2=4',
    'page': '1',
    'size': '10'
}
print(urlencode(data))
url = 'https://pbl.neoscholar.com/api/productpage/keti/searchListV2?' + urlencode(data)
response = requests.get(
    url=url,
    cookies=cookies,
    headers=headers,
)
print(response.text)