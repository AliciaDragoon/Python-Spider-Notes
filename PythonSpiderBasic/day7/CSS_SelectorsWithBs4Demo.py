import ssl
import time
import urllib.request
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = "https://desk.zol.com.cn/pc/"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/78.0.3904.97 Safari/537.36'}
ctx = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
ctx.options |= 0x4

add = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(url=add, timeout=10, context=ctx)

main_page_source = response.read().decode('gbk')
# print(main_page_source)

main_page = BeautifulSoup(main_page_source, "html.parser")
a_list = main_page.select(".photo-list-padding > a")
# print(len(a_list))
for a in a_list:
    href = a.get("href")
    if href.endswith(".exe"):
        continue
    href = urljoin(url, href)
    # print(href)
    child_resp = urllib.request.urlopen(url=href, timeout=10, context=ctx)
    child_source = child_resp.read().decode('gbk')
    child_page = BeautifulSoup(child_source, "html.parser")
    src = child_page.select_one("#bigImg").get("src")
    src_add = urllib.request.Request(url=src, headers=headers)
    img_resp = urllib.request.urlopen(url=src_add, timeout=10, context=ctx)
    file_name = src.split("/")[-1]
    with open(file_name, mode="wb") as f:
        f.write(img_resp.content)
    time.sleep(1)
