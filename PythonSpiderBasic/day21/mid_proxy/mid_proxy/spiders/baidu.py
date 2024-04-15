import scrapy


class BaiduSpider(scrapy.Spider):
    name = "baidu"
    allowed_domains = ["baidu.com"]
    start_urls = ["http://www.baidu.com/s?wd=ip"]

    def parse(self, resp, **kwargs):
        print(resp.text)
