import concurrent.futures
import requests

def download(url):
    r = requests.get(url)
    print(r)
    # 处理响应数据

urls = ['http://example.com', 'http://example.org', 'http://example.net']

with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [executor.submit(download, url) for url in urls]

for future in concurrent.futures.as_completed(futures):
    result = future.result()