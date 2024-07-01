#导入包
import  urllib.request


#设置请求头
headers={
'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
}
#设置请求地址
url="https://www.baidu.com/"

#通过urllib 创建请求对象
request =urllib.request.Request(url,headers=headers)
#通过urllib 执行请求
response =urllib.request.urlopen(request)

#获取read()方法会去请求响应内容 ，decode将响应内容解码
text=response.read().decode('utf-8')
#输出内容
print(text)

