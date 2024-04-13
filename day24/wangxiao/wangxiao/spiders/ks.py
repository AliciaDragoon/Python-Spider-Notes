import scrapy


class KsSpider(scrapy.Spider):
    name = "ks"
    allowed_domains = ["wangxiao.cn"]
    start_urls = ["http://ks.wangxiao.cn"]

    def parse(self, resp, **kwargs):
        # print(resp.url)
        # 解析页面结构
        li_list = resp.xpath("//ul[@class='first-title']/li")
        for li in li_list:
            first_title = li.xpath("./p/span/text()").extract_first()
            print(first_title)
