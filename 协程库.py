import gevent
import requests

def download(url):
    r = requests.get(url)
    print(r)
    # 处理响应数据

urls = ['http://example.com', 'http://example.org', 'http://example.net']

jobs = [gevent.spawn(download, url) for url in urls]
gevent.joinall(jobs)