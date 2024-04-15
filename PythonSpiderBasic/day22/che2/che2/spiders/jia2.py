import scrapy
from scrapy.linkextractors import LinkExtractor


# crawlspider(可控性较差)
class Jia2Spider(scrapy.Spider):
    name = "jia2"
    allowed_domains = ["che168.com"]
    start_urls = ["https://www.che168.com/beijing/a0_0msdgscncgpi1ltocsp1exx0/"]

    def parse(self, resp, **kwargs):
        # print(resp.url)
        # 使用LinkExtractor()函数获取页面上的所有链接
        lk1 = LinkExtractor(restrict_xpaths="//ul[@class='viewlist_ul']/li/a", deny_domains=("topicm.che168.com",))
        links = lk1.extract_links(resp)
        # print(links)
        for link in links:
            url = link.url
            text = link.text
            # print(url, text)
        lk2 = LinkExtractor(allow=r"beijing/a0_0msdgscncgpi1ltocsp\d+exx0")
        links2 = lk2.extract_links(resp)
        for link in links2:
            print(link.url)
