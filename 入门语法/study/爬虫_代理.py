import urllib.request

url = 'http://www.baidu.com'
headers= {
'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
}


request =urllib.request.Request(url, headers=headers)

handler = urllib.request.ProxyHandler()
opener = urllib.request.build_opener(handler)

response =opener.open(request)
data =response.read().decode('utf-8')
with open('baidu.html', 'w') as fp:
    fp.write(data)
    fp.close()