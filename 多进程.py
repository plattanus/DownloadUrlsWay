import multiprocessing
import requests

def download(url):
    r = requests.get(url)
    print(r)
    # 处理响应数据

urls = ['http://example.com', 'http://example.org', 'http://example.net']

processes = []
for url in urls:
    p = multiprocessing.Process(target=download, args=(url,))
    processes.append(p)
    p.start()

for p in processes:
    p.join()