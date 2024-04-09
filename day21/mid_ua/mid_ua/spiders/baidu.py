import scrapy


class BaiduSpider(scrapy.Spider):
    name = "baidu"
    allowed_domains = ["baidu.com"]
    start_urls = ["http://baidu.com"]

    def parse(self, resp, **kwargs):
        print(resp.request.headers)
