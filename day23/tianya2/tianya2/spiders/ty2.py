# 分布式爬虫：用redis队列替换scrapy的调度器
import scrapy
from scrapy_redis.spiders import RedisSpider

# 使用scrapy_redis提供的RedisSpider替换scrapy.spider
class Ty2Spider(RedisSpider):
    name = "ty2"
    allowed_domains = ["tianya.cn"]
    # start_urls = ["http://bbs.tianya.cn/list.jsp?item=free&order=1"]

    # 启动url
    redis_key = "ty2:urls"

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
        # print(txts)
        yield {"content": txt}


