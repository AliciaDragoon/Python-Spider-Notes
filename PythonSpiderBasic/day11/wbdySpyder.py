# 视频网站爬取视频
# 1 找到m3u8文件
# 2 眼看是否需要下载第二层m3u8
# 3 提取ts文件的下载路径
# 4 下载
# 5 是否需要解密
# 5.1 拿到密钥
# 5.2 解密
# 5.2.1 读取m3u8文件，获得文件名称和路径
# 5.2.2 每个ts文件分配一个解密任务
# 6 根据m3u8的播放顺序合并ts文件成mp4文件
import requests
from lxml import etree
import re
from urllib.parse import urljoin
import asyncio
import aiofiles
import aiohttp
from Crypto.Cipher import AES
import os

headers = {
    "User_Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/58.0.3029.110 Safari/537.3"
}


def get_iframe_src(url):
    resp = requests.get(url, headers=headers)
    tree = etree.HTML(resp.text)
    src = tree.xpath("//iframe/@src")[0]
    return src


def get_m3u8_url(url):
    resp = requests.get(url, headers=headers)
    # 使用re模块获取script标签内的内容
    obj = re.compile(r'url: "(?P<m3u8>.*?)"', re.S)
    m3u8 = obj.search(resp.text).group("m3u8")
    return m3u8


def download_m3u8(url):
    resp = requests.get(url, headers=headers)
    with open("first.m3u8", mode="w", encoding="utf-8") as f:
        f.write(resp.text)
    # 获取第二层m3u8地址
    with open("first.m3u8", mode="r", encoding="utf-8") as f2:
        for line in f2:
            if line.startswith("#"):
                continue
            line = line.strip()
            line = urljoin(url, line)
            resp = requests.get(line, headers=headers)
            with open("second.m3u8", mode="w", encoding="utf-8") as f3:
                f3.write(resp.text)
                break


async def download_one(url, sem):
    async with sem:  # 使用信号量限制协程的并发量，防止过载
        flag = True
        file_name = url.split("/")[-1]
        file_path = "./解密前/" + file_name
        print(file_name, "开始下载")
        for i in range(10):  # 下载失败的话重试
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(url, headers=headers) as resp:
                        content = await resp.content.read()
                        # 写入文件
                        async with aiofiles.open(file_path, mode="wb") as f:
                            await f.write(content)
                print(file_name, "下载完成")
                flag = False
                break
            except Exception as e:
                print(file_name, "出错了", e)  # 错误信息
        if flag:  # 保存下载失败的文件链接
            f = open("spyder.log", mode="a", encoding="utf-8")
            f.write(url)
            f.write("\n")


async def download_all_videos():
    # 使用信号量限制协程的并发量，防止过载
    sem = asyncio.Semaphore(100)  # 根据报错数量自行调节
    tasks = []
    # 读取文件
    with open("second.m3u8", mode="r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("#"):
                continue
            line = line.strip()  # 去除每一行最后的换行符，获取到下载地址
            # 创建任务
            t = asyncio.create_task(download_one(line, sem))
            tasks.append(t)
    # 统一等待
    await asyncio.wait(tasks)


def get_key():
    with open("second.m3u8", mode="r", encoding="utf-8") as f:
        file_content = f.read()
        obj = re.compile(r'URI="(?P<key_url>.*?)"')
        key_url = obj.search(file_content).group("key_url")
        resp = requests.get(key_url, headers=headers)
        return resp.content


async def desc_one(file_path, key):  # 解密文件
    file_name = file_path.split("/")[-1]
    new_file_path = "./解密后/" + file_name
    async with aiofiles.open(file_path, mode="rb") as f1, aiofiles.open("new_file_path", mode="wb") as f2:  # 读取f1，写入f2
        content = await f1.read()
        # 创建加密器
        aes = AES.new(key=key, mode=AES.MODE_CBC, IV=b"0000000000000000")  # 模式常用MODE_CBC和MODE_ECB
        # 解密
        new_content = aes.decrypt(content)
        await f2.write(new_content)


async def desc_all(key):
    tasks = []
    with open("second.m3u8", mode="r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("#"):
                continue
            line = line.strip()
            file_name = line.split("/")[-1]
            file_path = "./解密前/" + file_name
            # 创建解密任务
            t = asyncio.create_task(desc_one(file_path, key))
            tasks.append(t)
    await asyncio.wait(tasks)


def merge():
    # 合并指令
    # windows
    # copy /b a.ts+b.ts+c.ts "abc.mp4"
    # linux
    # cat a.ts+b.ts+c.ts > abc.mp4
    # 命令太长需要分批合并
    # 更换工作目录
    # 保存ts文件的顺序到列表
    file_list = []
    with open("second.m3u8", mode="r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("#"):
                continue
            line = line.strip()
            file_name = line.split("/")[-1]
            file_list.append(file_name)
    # 每20个文件合并一次
    os.chdir("./解密后")
    temp = []
    n = 1
    for i in range(len(file_list)):
        file_name = file_list[i]
        temp.append(file_name)
        if i != 0 and i % 20 == 0:
            cmd = f"copy /b {'+'.join(temp)} {n}.ts"
            r = os.popen(cmd)
            temp = []
            n = n + 1
    # 不足20个，单独合并
    cmd = f"copy /b {'+'.join(temp)} {n}.ts"
    r = os.popen(cmd)
    # 第二批合并
    last_temp = []
    for i in range(1, n + 1):
        last_temp.append(f"{i}.ts")
    cmd = f"copy /b {'+'.join(last_temp)} 春夏秋冬又一春.mp4"
    r = os.popen(cmd)
    # 切换至上一级文件夹
    os.chdir("../")


def main():
    url = "wbdy.tv/play/63690_1_1.html"
    # 获取iframe的src属性值
    src = get_iframe_src(url)
    # 发送请求到iframe的src路径，获取m3u8地址
    src = urljoin(url, src)
    m3u8_url = get_m3u8_url(src)
    # 下载m3u8文件
    download_m3u8(m3u8_url)
    # 下载视频
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(download_all_videos())
    # 获取密钥
    key = get_key()
    # 解密
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(desc_all(key))
    # 拼接成一个文件
    merge()


if __name__ == '__main__':
    main()
