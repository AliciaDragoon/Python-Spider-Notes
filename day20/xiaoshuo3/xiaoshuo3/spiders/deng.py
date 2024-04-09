import scrapy
from scrapy import Request


class DengSpider(scrapy.Spider):
    name = "deng"
    allowed_domains = ["17k.com"]
    start_urls = ["https://user.17k.com/ck/author2/shelf?page=1&appKey=2406394919"]

    # 模拟登录
    def start_requests(self):
        login_url = "https://passport.17k.com/ck/user/login"
        # scrapy发送post请求
        # yield scrapy.Request(
        #     url=login_url,
        #     method="POST",
        #     body="loginName=16538989670&password=q6035945",
        #     callback=self.login_success
        # )
        yield scrapy.FormRequest(
            url=login_url,
            method="POST",
            formdata={
                "loginName": "16538989670",
                "password": "q6035945",
            },
            callback=self.login_success
        )

    def login_success(self, resp, **kwargs):
        # print(resp.text)
        yield scrapy.Request(
            url=self.start_urls[0],
            callback=self.parse,
            dont_filter=True
        )

    def parse(self, resp, **kwargs):
        print(resp.text)
