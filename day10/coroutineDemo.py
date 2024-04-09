import asyncio


async def func():
    print("hello, async")

if __name__ == '__main__':
    f = func()
    # 方案1，直接运行，有可能会被Windows的事件管理器关闭
    # asyncio.run(f)
    # 方案2，创建一个事件循环再运行协程对象
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(f)
