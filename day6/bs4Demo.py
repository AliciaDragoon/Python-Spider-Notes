# 爬取https://desk.zol.com.cn/pc/上的图片
import ssl
import urllib.request
from bs4 import BeautifulSoup
from urllib.parse import urljoin

ctx = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
ctx.options |= 0x4  # OP_LEGACY_SERVER_CONNECT
# 绕过ssl检查

url = "https://desk.zol.com.cn/pc/"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/78.0.3904.97 Safari/537.36'}

# urllib添加headers
add = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(url=add, timeout=10, context=ctx)

main_page_source = response.read().decode('gbk')

main_page = BeautifulSoup(main_page_source, "html.parser")
# ul = main_page.find_all("ul", attrs={"class": "pic-list2"})
# find/find_all(标签, attrs={属性:值})
# print(len(ul))
# 2
# ul = main_page.find_all("ul", attrs={"class": "pic-list2"})[1]
# # 输出第二个ul

a_list = main_page.find("ul", attrs={"class": "pic-list2"}).find_all("a")
# 拿a标签的href
for a in a_list:
    href = a.get("href")  # get(属性)
    if href.endswith(".exe"):  # 判断字符串href是否以.exe结尾
        continue
    text = a.find("em").text  # 文本
    # print(href, text)
    href = urljoin(url, href)  # href并非完整的链接，使用urljoin()拼接链接
    # print(href, text)
    child_resp = urllib.request.urlopen(url=href, timeout=10, context=ctx)
    child_resp_source = child_resp.read().decode('gbk')
    child_page = BeautifulSoup(child_resp_source, "html.parser")
    src = child_page.find("img", attrs={"id": "bigImg"}).get("src")  # 可能会取到空值
    # print(src)
    img_resp = urllib.request.urlopen(url=src, timeout=10, context=ctx)
    file_name = src.split("/")[-1]
    with open(file_name, mode="wb") as f:
        # 下载图片
        f.write(img_resp.content)
    break  # 测试
    # 403
