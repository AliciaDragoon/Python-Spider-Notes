from scrapy.cmdline import execute

if __name__ == '__main__':
    execute("scrapy crawl ty2".split())

# scrapy_redis会把已经爬取成功到的url保存到redis的requests表中，下次启动时就不会爬已经爬到的url了
