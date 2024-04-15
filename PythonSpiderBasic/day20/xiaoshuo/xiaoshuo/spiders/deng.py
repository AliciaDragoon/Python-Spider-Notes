import scrapy


class DengSpider(scrapy.Spider):
    name = "deng"
    allowed_domains = ["17k.com"]
    start_urls = ["https://user.17k.com/ck/author2/shelf?page=1&appKey=2406394919"]

    def parse(self, resp, **kwargs):
        print(resp.text)
