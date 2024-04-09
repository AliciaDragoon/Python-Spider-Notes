import asyncio
import aiohttp  # 代替request
import aiofiles  # 代替open


async def download(url):
    print("准备下载：", url)
    file_name = url.split("/")[-1]
    # 发送请求
    # with后面用异步的包，一般前面要加async
    async with aiohttp.ClientSession() as session:  # requests.session()
        async with session.get(url) as resp:  # resp = session.get()，根据需要在括号内添加url，headers，data等参数
            content = await resp.content.read()  # 等待返回结果
            # # 获取页面源代码
            # page_source = await resp.text(encoding='utf-8')
            # # 获取json
            # dic = await resp.json()
            # # 同步代码获取字节
            # with open(file_name, mode="wb") as f:
            #     f.write(content)
            # 异步代码获取字节
            async with aiofiles.open(file_name, mode="wb") as f:
                await f.write(content)
    print("下载成功")


async def main():
    urls = [
        "https://xiuren.biz/wp-content/uploads/2023/01/BC205214344-04172815.jpg",
        "https://xiuren.biz/wp-content/uploads/2022/06/8317368998-01213749-01195638.jpg"
    ]  # 图片下载链接
    tasks = []
    for url in urls:
        tasks.append(asyncio.create_task(download(url)))
    await asyncio.wait(tasks)


if __name__ == '__main__':
    # asyncio.run(main())
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(main())
