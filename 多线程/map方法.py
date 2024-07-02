from multiprocessing import Pool

import requests



def scrape(url):
    try:
        print(requests.get(url))
    except ConnectionError:
        print('Error Occured ', url)
    finally:
        print('URL', url, ' Scraped')

if __name__ == '__main__':
      pool = Pool(processes=3)
      urls = [
          'https://www.baidu.com',
          'http://www.meituan.com/',
          'http://blog.csdn.net/',
          # 'http://xxxyxxx.net'
      ]
      pool.map(scrape, urls)
      pool.close()