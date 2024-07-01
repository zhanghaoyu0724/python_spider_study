import requests

cookies = {
    '__root_domain_v': '.youzhicai.com',
    '_qddaz': 'QD.951019239458173',
    '_qdda': '3-1.h84th',
    '_qddab': '3-w3zufm.lxt2s807',
    'Hm_lvt_9511d505b6dfa0c133ef4f9b744a16da': '1719239458',
    'Hm_lpvt_9511d505b6dfa0c133ef4f9b744a16da': '1719239458',
    'vue_admin_template_token': 'false',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': '__root_domain_v=.youzhicai.com; _qddaz=QD.951019239458173; _qdda=3-1.h84th; _qddab=3-w3zufm.lxt2s807; Hm_lvt_9511d505b6dfa0c133ef4f9b744a16da=1719239458; Hm_lpvt_9511d505b6dfa0c133ef4f9b744a16da=1719239458; vue_admin_template_token=false',
    'priority': 'u=0, i',
    'referer': 'https://www.youzhicai.com/s/5.html?key=%E5%8A%9E%E5%85%AC%E6%A5%BC',
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

response = requests.get(
    'https://www.youzhicai.com/nd/7a14c325-4be1-46eb-bf8d-a615882ffd1a-2.html',
    cookies=cookies,
    headers=headers,
)

print(response.text)