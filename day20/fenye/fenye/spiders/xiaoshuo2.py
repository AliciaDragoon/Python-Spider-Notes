import scrapy


class Xiaoshuo2Spider(scrapy.Spider):
    name = "xiaoshuo2"
    allowed_domains = ["17k.com"]
    start_urls = ["https://www.17k.com/all/book/2_0_0_0_0_0_0_0_1.html"]

    def parse(self, resp, **kwargs):
        trs = resp.xpath("//table/tbody/tr")
        # for tr in trs:
        #     leibie = tr.xpath("./td[2]//text()").extract()
        #     mingzi = tr.xpath("./td[3]//text()").extract()
        #     zuozhe = tr.xpath(".//[@class='zz'/a/text()]").extract_first()
        #     print(leibie, mingzi, zuozhe)
        # scrapy内置的翻页方法
        # 调度器中有一个用于去除重复的url的集合,一个请求队列。请求队列最后返回空，请求结束
        hrefs = resp.xpath("//div[@class='page']/a/@href").extract()
        for href in hrefs:
            if href.startswith("javascript"):
                continue
            href = resp.urljoin(href)
            # print(href)
            yield scrapy.Request(
                url=href,
                callback=self.parse,
                # dont_filter=True
                # 开启就不去重了
            )
