from multiprocessing import Process,Queue
from concurrent.futures import ThreadPoolExecutor
from lxml import etree
import time
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"
}

def get_img_src(url, q):
    """
    进程1: 负责提取页面中所有的img的下载地址
    将图片的下载地址通过队列. 传输给另一个进程进行下载
    """

    resp = requests.get(url, headers=headers)
    tree = etree.HTML(resp.text)
    srcs = tree.xpath("//li[@class='list-group-item']//img[@referrerpolicy='no-referrer']/@data-original")
    for src in srcs:
        q.put(src.strip())
    resp.close()



def download_img(q):
    """
        进程2: 将图片的下载地址从队列中提取出来. 进行下载.
   """
    with ThreadPoolExecutor(20) as t:
        while 1:
            try:
                s = q.get(timeout=20)
                t.submit(donwload_one, s)
            except Exception as e:
                print(e)
                break

def donwload_one(s):
    # 单纯的下载功能
    resp = requests.get(s, headers=headers)
    file_name = s.split("/")[-1]
    # 请提前创建好img文件夹
    with open(f"img/{file_name}", mode="wb") as f:
        f.write(resp.content)
    print("一张图片下载完毕", file_name)
    resp.close()

if __name__ == '__main__':
    t1 = time.time()
    q = Queue()  # 两个进程必须使用同一个队列. 否则数据传输不了
    p_list = []
    for i in range(1, 11):
        url = f"https://www.pkdoutu.com/photo/list/?page={i}"
        p = Process(target=get_img_src, args=(url, q))
        p_list.append(p)
    for p in p_list:
        p.start()
    p2 = Process(target=download_img, args=(q,))
    p2.start()
    for p in p_list:
        p.join()
    p2.join()
    print((time.time()-t1)/60)
# 0.49572664896647134