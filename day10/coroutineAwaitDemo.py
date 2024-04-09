import asyncio
import time


# 创建3个任务
async def func1():
    print("func1, start!")
    await asyncio.sleep(3)
    print("func1, finished!")


async def func2():
    print("func2, start!")
    await asyncio.sleep(4)
    print("func2, finished!")


async def func3():
    print("func3, start!")
    await asyncio.sleep(2)
    print("func3, finished!")


async def main():
    f1 = func1()
    f2 = func2()
    f3 = func3()
    # 把三个任务封装为任务对象
    t1 = asyncio.create_task(f1)
    t2 = asyncio.create_task(f2)
    t3 = asyncio.create_task(f3)
    tasks = [t1, t2, t3]
    # 挂起，等待任务执行结束
    await asyncio.wait(tasks)
    print("coroutine, finished!")


if __name__ == '__main__':
    s1 = time.time()
    asyncio.run(main())
    s2 = time.time()
    print(s2 - s1)