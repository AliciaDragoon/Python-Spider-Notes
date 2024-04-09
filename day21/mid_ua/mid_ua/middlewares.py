# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from mid_ua.settings import User_Agents,PROXIES
import random

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class MidUaSpiderMiddleware:
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


# 每次请求使用随机ua
class MidUaDownloaderMiddleware:
    def process_request(self, request, spider):
        # 获取ua
        # 随机抽选
        # 放到请求队列
        # 返回

        ua = random.choice(User_Agents)
        # 设置请求头
        request.headers['User-Agent'] = ua
        return None

# 每次请求使用随机ip
# class MidUaDownloaderMiddleware_proxy:
#     def process_request(self, request, spider):
#         ip = random.choice(PROXIES)
#         # 设置代理
#         request.meta['proxy'] = ip
#         return None
