from  bs4 import  BeautifulSoup


soup =BeautifulSoup(open('html/bs4.html'), 'lxml')

#根据标签名查找节点
#办找到的是第一个符合条件的数据#
# #print(soup.a)获取标签的属性和属性值
# print(soup.a.attrs)
# bs4的一些函数安效( 1 ) find返回的是第一个符合条件的数据乐
# print(soup.find('a'))

# print(soup.find('li',))

# limit 限制list数量
# print(soup.find_all('li', class_='a1'))


#select

# print(soup.select('li'))


#属性选择器
# #查找到li标签中有id的标签
print(soup.select( 'div,l'))

#节点信息并获取节点内容
obj = soup.select('#d1')[0]
# 如果标签对象中 只有内容 那么string和get_text()都可以使用
# #如果标签对象中除了内容还有标签 那么string就获取不到数据而get_text()是可以获取数据
# 我们一般情况下 推荐使用get_text()
print(obj.string)
print(obj.attrs)
