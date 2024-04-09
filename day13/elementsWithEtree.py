import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from lxml import etree

web = webdriver.Edge()
web.implicitly_wait(10)


def get_page_source(url):
    web.get(url)
    time.sleep(3)
    return web.page_source
    # 返回的是elements


if __name__ == '__main__':
    url = ('https://search.bilibili.com/all?keyword=%E9%A9%AC%E5%BE%B7%E9%87%8C%E5%A4%A7%E5%B8%88%E8%B5%9B'
           '&search_source=1')
    page_source = get_page_source(url)
    tree = etree.HTML(page_source)
    txt = tree.xpath("//*[@class='video-list row']//text()")
    print(txt)
