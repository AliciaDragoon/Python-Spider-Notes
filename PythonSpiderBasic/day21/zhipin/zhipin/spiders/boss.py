from typing import Iterable

import scrapy
from scrapy import Request
from zhipin.req import SeleniumRequest

class BossSpider(scrapy.Spider):
    name = "boss"
    allowed_domains = ["zhipin.com"]
    start_urls = ["https://www.zhipin.com/web/geek/job?query=python&city=101010100&page=2"]

    def start_requests(self) -> Iterable[Request]:
        # 使用selenium请求
        yield SeleniumRequest(url=self.start_urls[0], dont_filter=True)
        # 普通请求
        # yield scrapy.Request(url=self.start_urls[0])
        yield scrapy.Request(url="https://www.baidu.com/", dont_filter=True)
    def parse(self, resp, **kwargs):
        print("我是parse", resp.url)
