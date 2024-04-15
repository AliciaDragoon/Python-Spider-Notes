import scrapy


class JiaSpider(scrapy.Spider):
    name = "jia"
    allowed_domains = ["che168.com"]
    start_urls = ["https://www.che168.com/beijing/a0_0msdgscncgpi1ltocsp1exx0/"]

    # 映射结构
    che_biaozhun = {
        "表显里程": "licheng",
        "上牌时间": "shijian",
        "挡位/排量": "pailiang",
        "车辆所在地": "suozaidi",
        "查看限迁地": "biaozhun",
    }

    # 解析start_urls
    def parse(self, resp, **kwargs):
        # 测试请求是否通畅
        # print(resp.url)
        li_list = resp.xpath("//ul[@class='viewlist_ul']/li")
        for li in li_list:
            href = li.xpath("./a/@href").extract_first()
            href = resp.urljoin(href)
            # 过滤广告
            if "topicm" in href:
                continue
            # print(href)
            yield scrapy.Request(
                url=href,
                callback=self.parse_detail
            )

            # 提取分页
            hrefs = li.xpath("//div[@id='listpagination']/a/@href").extract()
            for href in hrefs:
                if href.startswith("javascript"):
                    continue
                # print(href)
                href = resp.urljoin(href)
                yield scrapy.Request(
                    url=href,
                    callback=self.parse
                )
                # 翻到下一页再执行一次parse函数


    # 解析详情页
    def parse_detail(self, resp, **kwargs):
        # 函数执行时才知道详情页的请求有无响应，响应的顺序
        name = resp.xpath("//div[@class='car-box']/h3/text()").extract_first()
        # print(name)
        li_list = resp.xpath("//div[@class='car-box']/ul/li")
        dic: dict = {
            "licheng":"未知",
            "shijian":"未知",
            "pailiang":"未知",
            "suozaidi":"未知",
            "biaozhun":"未知"
        }
        # 设置字典默认值

        for li in li_list:
            p_name = li.xpath("./p//text()").extract_first()
            p_value = li.xpath("./h4/text()").extract_first()
            # print(p_name, p_value)
            p_name = p_name.replace(" ","").strip()
            p_value = p_value.replace(" ", "").strip()

            data_key =self.che_biaozhun[p_name]
            dic[data_key] = p_value
        # print(dic)
        yield dic

