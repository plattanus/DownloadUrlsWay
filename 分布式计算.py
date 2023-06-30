from pyspark.sql import SparkSession
import requests

def download(url):
    r = requests.get(url)
    print(r)
    # 处理响应数据
    return url, r.content

urls = ['http://example.com', 'http://example.org', 'http://example.net']

spark = SparkSession.builder.appName('download').getOrCreate()

rdd = spark.sparkContext.parallelize(urls)
result = rdd.map(download).collect()

for url, content in result:
    pass
    # 处理下载结果