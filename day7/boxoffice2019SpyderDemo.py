# //table/tbody/tr
import requests
from lxml import etree

url = "http://www.boxofficecn.com/boxoffice2019"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"}
resp = requests.get(url, headers=headers)
# print(resp.text)
page = etree.HTML(resp.text)
trs = page.xpath("//table/tbody/tr")[1:-1]  # 第一行是表头，最后一行是空
# print(len(trs))
for tr in trs:
    num = tr.xpath("./td[1]/text()")
    year = tr.xpath("./td[2]//text()")
    name = tr.xpath("./td[3]//text()")[0]
    # 083, 093, 191, 312数据为空
    if name:
        "".join(name).replace("\x0a", "")  # 合并数据并去除换行符
    money = tr.xpath("./td[4]/text()")
    print(num, year, name, money)
