import asyncio
import aiohttp

async def download(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(response)
            # 处理响应数据

urls = ['http://example.com', 'http://example.org', 'http://example.net']

loop = asyncio.get_event_loop()
tasks = [loop.create_task(download(url)) for url in urls]
loop.run_until_complete(asyncio.wait(tasks))