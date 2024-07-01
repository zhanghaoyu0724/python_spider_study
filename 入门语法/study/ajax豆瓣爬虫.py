import json
import urllib.request


def get_douban_movie(i):
    start = i*20;
    url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start='+str(start)+'&limit=20'
    print(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
    }

    data = {

    }
    request = urllib.request.Request(url=url, headers=headers)

    response = urllib.request.urlopen(request);

    content = response.read().decode('utf-8')

    with open('douban.txt', 'a') as fp:
        movies = json.loads(content)
        for movie in movies:
            print(type(movie))
            title = movie['title']
            fp.write(title+'\n')
        fp.close()


if __name__ == '__main__':
    for i in range(10):
        get_douban_movie(i)
