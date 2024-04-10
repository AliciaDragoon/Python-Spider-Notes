# 天涯论坛暂时关闭--2024/4/9
import scrapy


# 增量式爬虫
class TySpider(scrapy.Spider):
    name = "ty"
    allowed_domains = ["tianya.cn"]
    start_urls = ["http://bbs.tianya.cn/list.jsp?item=free&order=1"]

    def parse(self, resp, **kwargs):
        tbodys = resp.xpath("//div[@class='mt5']/table/tbody")
        # print(len(tbodys))
        for tbody in tbodys:
            trs = tbody.xpath("./tr")
            for tr in trs:
                title = tr.xpath("./td[1]/a/text()")[0].extract_first().s
                # print(title)
                href = tr.xpath("./td[1]/a/@href")[0].extract_first()

                yield scrapy.Request(
                    url=href,
                    callback=self.parse_detail
                )
    def parse_detail(self, resp, **kwargs):
        txts = resp.xpath("//div[@class='bbs-content clearfix']//text()").extract()
        txt = "".join(txts)
        txt = txt.strip()
        # print(txt)
