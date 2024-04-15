import scrapy


class My4399Spider(scrapy.Spider): # 继承了scrapy的Spider
    name = "my4399"
    # spider的名字
    allowed_domains = ["4399.com"]
    # 限制该spider抓取的域名
    start_urls = ["https://www.4399.com/flash/game100.htm"]
    # 引擎工作时，把起始url自动包装成一个请求对象
    # 引擎开始调度，交给下载器获取页面源代码，封装成响应对象
    # 最后把响应对象交给spider(解析函数parse)解析

    # 解析start_urls返回的响应
    def parse(self, resp, **kwargs):
        # resp: 响应对象
        # 在settings中设置LOG_LEVEL = "WARNING", ROBOTSTXT_OBEY = False
        # print(resp.text)
        li_list = resp.xpath("//*[@id = 'list']/li")
        # srcrapy使用parsel解析页面源代码
        for li in li_list:
            # name = li.xpath("./div[1]/a//text()").extract()[0]
            # 提取器：extract()
            name = li.xpath("./div[1]/a//text()").extract_first()
            # extract_first()可以提取第一个，可避免越界。空内容会返回None
            # print(name)
            leibie = li.xpath("./span[1]/a/text()").extract_first()
            # print(leibie)
            shijian = li.xpath("./span[2]/text()").extract_first()
            # print(name, leibie, shijian)
            yield {"name":name, "leibie": leibie, "shijian": shijian}
            # 生成器函数yield可以在返回一条数据后，继续运行函数
            # scrapy规定yield只能返回字典, item(去pipline保存数据);request(去调度器请求队列);None(结束)。