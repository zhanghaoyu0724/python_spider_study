
#https://sc.chinaz.com/tupian/index.html 1
# https://sc.chinaz.com/tupian/index_2.html

import urllib.request
from lxml import etree

def create_request(page):
    if(page == 1):
        url ='https://sc.chinaz.com/tupian/index.html'
    else:
        url = 'https://sc.chinaz.com/tupian/index_'+str(page)+'.html'
    return urllib.request.Request(url)

def get_images(url):
    image_name =url.rpartition('/')[2]
    request = urllib.request.Request(url)
    response =urllib.request.urlopen(request)
    image_byte=response.read()
    with open('./img/'+image_name,'wb') as fp:
        fp.write(image_byte)
        fp.close()

if __name__ == '__main__':
    request=create_request(2)
    res = urllib.request.urlopen(request)
    html = res.read().decode('utf-8')
    etree =etree.HTML(html)
    list_images=etree.xpath("//html//img[@class='lazy']/@data-original")
    for image in list_images:
    # image=list_images[0]
        image_url='https:'+str(image)
        print(image_url)
        get_images(image_url)



