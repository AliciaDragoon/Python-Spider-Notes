import scrapy
from cai.items import CaiItem


class SsqSpider(scrapy.Spider):
    name = "ssq"
    allowed_domains = ["sina.com.cn"]
    start_urls = ["https://view.lottery.sina.com.cn/lotto/pc_zst/index?lottoType=ssq&actionType=chzs"]

    def parse(self, resp, **kwargs):
        # print(resp.text)
        # 注意检查想要的数据在不在页面源代码
        trs = resp.xpath("//*[@id ='cpdata']/tr")
        for tr in trs:
            red_ball = tr.xpath("./td[@class='chartball01' or @class = 'chartball20']/text()").extract()
            if not red_ball:
                continue
            # print(red_ball)
            blue_ball = tr.xpath("./td[@class='chartball02']/text()").extract_first()
            # print(blue_ball)
            qi = tr.xpath("./td[1]/text()").extract_first()
            # print(qi, red_ball, blue_ball)

            # yield {
            #     "qi": qi,
            #     "red_ball": red_ball,
            #     "blue_ball": blue_ball
            # }
            # 官方推荐使用item约束返回值，见items.py
            cai = CaiItem()
            cai["qi"] = qi
            cai["red_ball"] = red_ball
            cai["blue_ball"] = blue_ball
            yield cai
