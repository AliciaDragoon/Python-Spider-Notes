import requests
from lxml import etree
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Process, Queue  # 进程, 队列


def get_img_url():  # 进程1: 获取图片链接
    for page in range(1, 11):
        url = f"https://www.pkdoutu.com/article/list/?page={page}"
        headers = {
            "User-Agent":
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 "
                "Safari/537.36 Edg/120.0.0.0",
        }
        resp = requests.get(url, headers=headers)
        tree = etree.HTML(resp.text)
        img_urls = tree.xpath(
            "//li[@class= 'list-group-item']//img/@data-original")  # 图片存储在data-original中，而不是页面源代码的src中
        # with ThreadPoolExecutor(16) as t:
        #     for img_url in img_urls:
        #         # print(img_url)
        #         t.submit(download_img, img_url)
        for img_url in img_urls:
            # print(img_url)
            # download_img(img_url)
            q.put(img_url)  # 把图片地址塞入队列
    q.put("已获取全部链接")


def img_process(q):  # 进程2: 从队列q中提取img_url并下载
    with ThreadPoolExecutor(16) as t:
        while 1:
            img_url = q.get()
            if img_url == "已获取全部链接":
                break
            t.submit(download_img, q.get())  # 进程中开启多线程


def download_img(url):  # 下载图片
    headers = {
        "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 "
            "Safari/537.36 Edg/120.0.0.0",
    }
    resp = requests.get(url, headers=headers)
    file_name = url.split("/")[-1]
    with open(file_name, mode="wb") as f:
        f.write(resp.content)
    print("已下载一张图片")


if __name__ == '__main__':  # 生产-消费模型
    q = Queue()
    p1 = Process(target=get_img_url, args=(q,))
    p2 = Process(target=img_process, args=(q,))

    p1.start()
    p2.start()
