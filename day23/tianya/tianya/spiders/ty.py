import scrapy

# 增量式爬虫
class TySpider(scrapy.Spider):
    name = "ty"
    allowed_domains = ["tianya.cn"]
    start_urls = ["http://bbs.tianya.cn/list.jsp?item=free&order=1"]
    # 天涯论坛暂时关闭 2024/4/9
    def parse(self, resp, **kwargs):
        pass
