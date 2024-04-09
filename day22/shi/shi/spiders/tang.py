import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TangSpider(CrawlSpider):
    name = "tang"
    allowed_domains = ["shicimingjv.com"]
    start_urls = ["https://www.shicimingjv.com/tangshi/index_1.html"]

    # 链接提取器提取详情页的url
    lk1 = LinkExtractor(restrict_xpaths="//div[@class='article-list']/ul/li/div/h3/a")
    rules = (
        Rule(lk1, callback="parse_item", follow=True),
    )

    def parse_item(self, response):
        item = {}
        #item["domain_id"] = response.xpath('//input[@id="sid"]/@value').get()
        #item["name"] = response.xpath('//div[@id="name"]').get()
        #item["description"] = response.xpath('//div[@id="description"]').get()
        return item
