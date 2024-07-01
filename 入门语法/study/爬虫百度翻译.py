import urllib.request
import  urllib.parse
from copyheaders import headers_raw_to_dict
#
# url = 'https://fanyi.baidu.com/sug'
#
# headers= {
# 'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
# }
# data ={
# 'kw': 'spider'
# }
#
# data = urllib.parse.urlencode(data).encode('utf-8')
#
# request= urllib.request.Request(url = url, data=data, headers = headers)
#
# response = urllib.request.urlopen(request)
# content = response.read().decode('utf-8')
#
# import  json
#
# print(json.loads(content))
r_h='''

'''
headers = headers_raw_to_dict(r_h)
