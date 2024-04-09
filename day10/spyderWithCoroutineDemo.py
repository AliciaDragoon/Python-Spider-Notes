import asyncio
import time


async def get_page_source(url):
    # 模拟网络请求
    print("请求", url)
    await asyncio.sleep(3)
    print("响应")
    return "页面源代码"


async def main():
    urls = [
        "http://www.baidu.com",
        "http://www.taobao.com",
        "http://www.google.com",
        "http://www.jd.com",
    ]
    # 可通过request获取主页的页面源代码，再通过lxml获取分页的下载地址
    tasks = []
    for url in urls:
        f = get_page_source(url)
        t = asyncio.create_task(f)
        tasks.append(t)

    # await asyncio.wait(tasks)

    # 获取url的页面源代码
    # result, pending = await asyncio.wait(tasks)
    # for r in result:
    #     print(r.result())

    result = await asyncio.gather(*tasks)
    for r in result:
        print(r)


if __name__ == '__main__':
    s1 = time.time()
    asyncio.run(main())
    s2 = time.time()
    print(s2 - s1)
