from lxml import etree

tree = etree.parse('解析xPath_基本使用.html')

# // 表示子孙节点 /儿子节点
#


#查找ID=shanghaide li标签的内容值
# li_list = tree.xpath('//body//li[@id="shanghai"]/text()')
#查找ID=shanghaide li标签的属性值
# li_list = tree.xpath('//body//li[@id="shanghai"]/@name')
li_list = tree.xpath('//body//li[contains(@id,"z")]/text()')
print(li_list)