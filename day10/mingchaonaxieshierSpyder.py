# 需求
# 每一部放一个文件夹，每章放一个txt
# 首先，获取主页面的源代码
# 然后，解析<卷名>, <章节, href>
import requests
from lxml import etree
import asyncio
import aiohttp
import aiofiles
import os

# 以字典{
#     'chapter_name': '洪武大帝前言',
#     'chapter_url': 'https://www.mingchaonaxieshier.com/hong-wu-da-di-qianyan.html',
#     'juanming': '明朝那些事儿1_洪武大帝'
# }
# 的格式保存章节名，章节链接，卷名
headers = {
        "user-agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / "
                      "121.0.0.0Safari / 537.36Edg / 121.0.0.0"
    }
def get_chapter_info(url):
    result = []
    resp = requests.get(url, headers=headers)
    resp.encoding = "UTF-8"
    page_source = resp.text
    # 检查中文是否乱码
    # print(page_source)
    # 开始解析
    tree = etree.HTML(page_source)
    # <div class="mulu">
    # 爬取每一卷
    divs = tree.xpath("//div[@class= 'mulu']")
    # print(len(divs))
    # 共7卷
    # <table> <tr>
    # <td colspan="3"><center><h2>
    # <a href="https://www.mingchaonaxieshier.com/ming-chao-na-xie-shi-er-1">明朝那些事儿1：洪武大帝</a></h2></center></td>
    # 爬取卷名
    for div in divs:
        trs = div.xpath(".//table/tr")
        juanming = trs[0].xpath(".//a/text()")
        juanming = "".join(juanming).strip().replace("：", "_")
        # print(juanming)
        # <tr> <td>
        # <a href="https://www.mingchaonaxieshier.com/hong-wu-da-di-qianyan.html">洪武大帝 前言</a></td>
        # 爬取每一章的章节名和链接
        for tr in trs[1:]:
            tds = tr.xpath("./td")
            for td in tds:
                txt = td.xpath(".//text()")
                href = td.xpath(".//@href")
                # print(txt, href)
                # ['洪武大帝 前言']
                txt = "".join(txt).replace(" ", "").strip()
                # repalce()替换时要手动复制旧项，防止特殊符号不显示
                href = "".join(href)
                dic = {
                    "chapter_name": txt,
                    "chapter_url": href,
                    "juanming": juanming
                }
                # print(dic)
                result.append(dic)
    return result

async def download_one(url, file_path):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers= headers) as resp:
            page_source = await resp.text(encoding="UTF-8")
            tree = etree.HTML(page_source)
            # 获取文章
            # <div class="content" >
            # ...
            #   <p>好了，今天晚上开始工作吧！</p>
            # ...
            content = tree.xpath("//div[@class='content']//p//text()")
            content = "".join(content).replace("\n", "").replace("\r","").replace(" ", "").strip()
            # 写入文件
            async with aiofiles.open(file_path, mode="w", encoding="UTF-8") as f:
                await f.write(content)
    print("已下载一篇")

async def download_chapter(chapter_list):
    tasks = []
    for chapter in chapter_list:
        juan = chapter['juanming'] # 文件夹名
        name = chapter['chapter_name'] # 文件名
        url = chapter['chapter_url']

        if not os.path.exists(juan): # 判断文件夹是否存在
            os.makedirs(juan) # 不存在就创建一个
        file_path = f"{juan}/{name}.txt"
        t = asyncio.create_task(download_one(url, file_path))
        tasks.append(t)
        # break
    await asyncio.wait(tasks)
def main():
    url = "https://www.mingchaonaxieshier.com/"
    chapter_list = get_chapter_info(url)
    # print(chapter_list)
    # 异步下载
    asyncio.run(download_chapter(chapter_list))

if __name__ == '__main__':
    main()
