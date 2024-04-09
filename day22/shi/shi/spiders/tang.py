import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TangSpider(CrawlSpider):
    name = "tang"
    allowed_domains = ["shicimingjv.com"]
    start_urls = ["https://www.shicimingjv.com/tangshi/index_1.html"]

    # 链接提取器提取详情页的url
    lk1 = LinkExtractor(restrict_xpaths="//div[@class='sec-panel-body']/ul/li/div/h3/a")
    # 提取页码的url
    lk2 = LinkExtractor(restrict_xpaths="//ul[@class='pagination']/li/a")
    rules = (
        # crawlspider会自动发送请求，并提取链接（完成了parse的工作）
        Rule(lk1, callback="parse_item"),
        Rule(lk2, follow=True),
        # follow=True表示重新来一遍
    )

    # 提取唐诗的标题
    def parse_item(self, response, **kwargs):
        title = response.xpath("//h1[@class='mp3']/text()").extract_first()
        print(title)
        # 共120首
