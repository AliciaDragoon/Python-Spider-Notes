import requests
from lxml import etree
from concurrent.futures import ThreadPoolExecutor
import time


def str_tool(lst):
    if lst:
        s = "".join(lst)
        return s.strip()
    else:
        return ""
    # 去除特殊字符


def get_movie_info(year):
    f = open(f"{year}.csv", mode="w", encoding="utf-8")
    url = f"http://www.boxofficecn.com/boxoffice{year}"
    headers = {
        "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 "
            "Safari/537.36 Edg/120.0.0.0",
    }
    resp = requests.get(url, headers=headers)
    tree = etree.HTML(resp.text)
    trs = tree.xpath("//table/tbody/tr")[1:]

    for tr in trs:
        num = tr.xpath("./td[1]/text()")
        year = tr.xpath("./td[2]//text()")
        name = tr.xpath("./td[3]//text()")
        money = tr.xpath("./td[4]/text()")

        num = str_tool(num)
        year = str_tool(year)
        name = str_tool(name)
        money = str_tool(money)

        # print(num, year, name, money)
        f.write(f"{num}, {year}, {name}, {money}\n")


if __name__ == '__main__':
    # s1 = time.time()
    # for y in range(1994, 2023):
    #     get_movie_info(y)
    #     # t1 = threading.Thread(target=get_movie_info, args=(y,))
    #     # t1.start()
    # s2 = time.time()
    # print(s2-s1)
    # # 单线程耗时长
    s1 = time.time()
    with ThreadPoolExecutor(16) as t:
        for y in range(1994,2023):
            t.submit(get_movie_info, y)
    s2 = time.time()
    print(s2-s1)
    # 线程池耗时短
