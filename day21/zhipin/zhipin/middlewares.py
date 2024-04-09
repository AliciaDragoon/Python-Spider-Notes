# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
from scrapy.http import HtmlResponse
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from zhipin.req import SeleniumRequest



class ZhipinSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class ZhipinDownloaderMiddleware:
    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        # 爬虫开始时执行
        crawler.signals.connect(s.spider_closed, signal=signals.spider_closed)
        # 爬虫结束时执行
        return s



    def process_request(self, request, spider):
        if isinstance(request, SeleniumRequest):
            print("我是selenium")
            # 使用selenium爬取页面源代码的elements
            self.web.get(request.url)
            # time.sleep(2)
            self.web.find_element(By.XPATH, '//*[@id="wrap"]/div[2]/div[2]/div/div[2]/div[2]/a')
            # time.sleep(2)
            page_source = self.web.page_source

            # 组装响应对象
            resp = HtmlResponse(
                status=200,
                url=request.url,
                body=page_source.encode('utf-8'),
                request=request
            )
            return resp
        else:
            print("我是普通")
            return None

    def process_response(self, request, response, spider):
        return response
    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)
        self.web = webdriver.Edge()
        self.web.implicitly_wait(10)

    def spider_closed(self, spider):
        self.web.close()