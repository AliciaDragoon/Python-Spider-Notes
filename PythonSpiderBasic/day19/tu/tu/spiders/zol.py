import scrapy


class ZolSpider(scrapy.Spider):
    name = "zol"
    allowed_domains = ["zol.com.cn"]
    start_urls = ["https://desk.zol.com.cn/dongman/"]

    def parse(self, resp, **kwargs):
        # print(resp.text)
        # 获取图片详情页的url
        a_list = resp.xpath("//*[@class='pic-list2  clearfix']/li/a")
        for a in a_list:
            # print(a.xpath("./@href").extract_first())
            href = a.xpath("./@href").extract_first()
            if href.endswith(".exe"):
                continue
            # print(href)
            href = resp.urljoin(href)
            # scrapy自带的域名拼接方法(resp.url+href)
            # print(href)

            yield scrapy.Request(
                url=href,
                method="get",
                callback=self.hd_parse_detail
            )

    # 返回清晰度列表第一个选项的图片链接（即清晰度最高的那个）
    def hd_parse_detail(self, resp, **kwargs):
        hd_src = resp.xpath("//*[@id='tagfbl']/a[1]/@href").extract_first()
        hd_src = resp.urljoin(hd_src)
        if hd_src.endswith(".html"):
            # print(hd_src)
            yield scrapy.Request(
                url=hd_src,
                method="get",
                callback=self.hd_img_parse_detail
            )

    def hd_img_parse_detail(self, resp, **kwargs):
        hd_img_src = resp.xpath("//img/@src").extract_first()
        # print(hd_img_src)
        yield {"img_src": hd_img_src}
