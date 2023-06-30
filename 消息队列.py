import redis
import requests

def download(url):
    r = requests.get(url)
    print(r)
    # 处理响应数据

urls = ['http://example.com', 'http://example.org', 'http://example.net']

r = redis.Redis(host='localhost', port=6379)

for url in urls:
    r.lpush('download_queue', url)

while True:
    url = r.rpop('download_queue')
    if url is None:
        break
    download(url)