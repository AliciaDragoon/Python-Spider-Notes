# 验证代理ip有效性
# 查找redis中存储的所有ip
# 使用协程挨个发送请求，请求成功则给满分，不成功扣1分
from proxy_redis import ProxyRedis
import asyncio
import aiohttp
import time
from settings import *

url = "https://www.baidu.com/"


# 或采取你要爬取的网站

async def verify_one(ip, sem, red):
    print(f"正在检测{ip}的可用性")
    timeout = aiohttp.ClientTimeout(total=10)
    # 超时时间设置为10s
    async with sem:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, proxy="http://" + ip, timeout=timeout) as resp:
                    page_source = await resp.text()
                    if resp.status in [200, 302]:
                        # 访问正常
                        red.set_max_score(ip)
                        print(f"检测到{ip}可用，给100分")
                    else:
                        # 超时
                        red.desc_incrby(ip)
                        print(f"检测到{ip}访问超时，扣1分")
        except Exception as e:
            print("校验出现错误", e)
            red.desc_incrby(ip)
            print(f"检测到{ip}访问超时，扣1分")


async def main(red):
    # 查询所有ip
    all_proxies = red.get_all_proxy()

    sem = asyncio.Semaphore(SEM_COUNT)
    tasks = []
    for ip in all_proxies:
        tasks.append(asyncio.create_task(verify_one(ip, sem, red)))
    await asyncio.wait(tasks)


def run():
    red = ProxyRedis()
    time.sleep(START_VERIFY_WAIT_TIME)
    while 1:
        try:
            asyncio.run(main(red))
            time.sleep(100)
            # 休眠
        except Exception as e:
            print("校验出现错误", e)
            time.sleep(100)


if __name__ == '__main__':
    run()
