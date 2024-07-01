import json

import execjs

# 获取音乐接口
#https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token=
from  requests_html import HTMLSession
session = HTMLSession()

with open('wyy_music.js', 'r') as f:
    ctx = execjs.compile(f.read())
data =["流泪", "强"]
params =ctx.call('getData')
headers={
    'Content-Type':'application/x-www-form-urlencoded',
    'Cookie':'NMTID=00OoNeAcUKtm0bHhE7IoFh4DMDJYyYAAAGQRTSUKg; _iuqxldmzr_=32; _ntes_nnid=c22d3b7aa6df9f0147c9a5c2ce0617f5,1719147992253; _ntes_nuid=c22d3b7aa6df9f0147c9a5c2ce0617f5; WEVNSM=1.0.0; WNMCID=dccbmr.1719147992745.01.0; WM_NI=VKIS0KePkBY9cUdDExFx4gC1SEpxd9Sm9tfoO4OfHIq11gVvxQ7zPG7BxahnpF1Wh0DVmpI80Qbs%2BaCGwNu7gVYqOvTZ0jGnaulZ9e4F16J5g7JgKmsyZF%2BmiFUgCS8jNnE%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eea6c63bf695e58bf5708ae78ab2d55e968e8fadd24a858fa2b5e95d95befe82f32af0fea7c3b92a969587b4b341a790a5a3dc33a18baca5c87486a8fc88c23b919bc099e73391b3f795e5658dec8187cb43b3efff88d57ebc8ff99bd34df59eb882eb66b49affb8eb3c888aa391cc34f48fae94aa6b8199b9aff83da58a9792ce7e9886008bc666a3aba4bbbc6ff89affd7c93fa5e98688ca67b1a796a7aa67ab9a9b88c259fcb6828fc837e2a3; WM_TID=KYbQ2XV4qkZABVFUFUaHBTQ3XnTDeiL4; sDeviceId=YD-iAhEBZpn499FRwUAABOGAXQjHnXdJGNd; ntes_utid=tid._.m5sQz1zsiJZBVxEAAFfHVSAmH3WdNHIB._.0; playerid=19664825; JSESSIONID-WYYY=KM%5CV0a0OklnVkuIU32SEMHjwWlbWivnR33EdF%2BnKkgFm%2FDQ43%5CAnospb%2FgOFNkP3eg5FeCUOQ9Xcgavgb4kqScFINAi5ozRXmyzi%2B5tBC0xHIV1H%5CKAG7oUwdFWgZutRWOmiNtxVyDPz8TRQP72%5CDEjHy%5C%5CcBsH7xhya2l%5CZRbvdie45%3A1719151532372',
    'Origin':'https://music.163.com',
    'Referer':'https://music.163.com/',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}
url='https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token='

result_data= {'params': params['encText'],'encSecKey': params['encSecKey']}
print(result_data)
response =session.post(url=url, data=result_data,headers=headers).json()
print(response)