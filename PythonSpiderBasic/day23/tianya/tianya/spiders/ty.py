# 天涯论坛暂时关闭--2024/4/9
import scrapy
from scrapy import signals
from redis import Redis


# 增量式爬虫（利用redis去除重复的url和内容）
class TySpider(scrapy.Spider):
    name = "ty"
    allowed_domains = ["tianya.cn"]
    start_urls = ["http://bbs.tianya.cn/list.jsp?item=free&order=1"]

    # 绑定事件
    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(s.spider_closed, signal=signals.spider_closed)
        return s

    # 在scrapy.spider开始时建立redis连接
    def spider_opened(self, spider):
        self.coon = Redis(
            host='127.0.0.1',
            port=6379,
            db=2,
            decode_responses=True
        )

    # 在scrapy.spider结束时关闭redis连接
    def spider_closed(self, spider):
        if self.coon:
            self.coon.close()

    def parse(self, resp, **kwargs):
        # 获取所有帖子
        tbodys = resp.xpath("//div[@class='mt5']/table/tbody")[1:]
        # print(len(tbodys))
        for tbody in tbodys:
            trs = tbody.xpath("./tr")
            for tr in trs:
                # 获取每条帖子的标题和链接
                title = tr.xpath("./td[1]/a/text()")[0].extract_first()
                # print(title)
                href = tr.xpath("./td[1]/a/@href")[0].extract_first()
                href = resp.urljoin(href)

                t = self.coon.sismember("ty:urls", href)
                if t:
                    print("已全部抓取，没有新的帖子")
                else:
                    yield scrapy.Request(
                        url=href,
                        callback=self.parse_detail,
                        meta={"href": href}
                        # 可以在meta中传递一个变量，控制爬取的页数
                    )

    def parse_detail(self, resp, **kwargs):
        # 获取每条帖子的正文
        href = resp.meta["href"]
        # 通过meta传递可以避免重定向导致的访问问题
        txts = resp.xpath("//div[@class='bbs-content clearfix']//text()").extract()
        txt = "".join(txts)
        txt = txt.strip()
        # print(txt)
        self.coon.sadd("ty:urls", href)
        yield {"content": txt}
