import threading
import requests

def download(url):
    r = requests.get(url)
    # 处理响应数据
    print(r)
    

urls = ['http://example.com', 'http://example.org', 'http://example.net']

threads = []
for url in urls:
    t = threading.Thread(target=download, args=(url,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()