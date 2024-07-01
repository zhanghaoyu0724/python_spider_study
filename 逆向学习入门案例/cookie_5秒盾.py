import requests
from curl_cffi import requests

cookies = {
    '__cf_bm': '.R_ih6hzZSrNJcPvSsnRMgIkR1giROH3db7MGE4Quw8-1719237459-1.0.1.1-wR4LZmfI4Yx5XH6Pp7pbMpmN1e.w8E2VXA9pC3Bza7G46uJtBuoETzjWZ2vz4xC_2ZRdjxplJzZLZ7cakj.rCg',
}
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': '__cf_bm=.R_ih6hzZSrNJcPvSsnRMgIkR1giROH3db7MGE4Quw8-1719237459-1.0.1.1-wR4LZmfI4Yx5XH6Pp7pbMpmN1e.w8E2VXA9pC3Bza7G46uJtBuoETzjWZ2vz4xC_2ZRdjxplJzZLZ7cakj.rCg',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

#TLS 第三方库检测 设备指纹检测 标准
response = requests.get('https://radar.cloudflare.com/traffic/verified-bots', impersonate='edge101',cookies=cookies, headers=headers)
print(response.content.decode())