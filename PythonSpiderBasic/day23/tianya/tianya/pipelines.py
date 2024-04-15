# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy import signals
from redis import Redis


# 去除重复的内容
class TianyaPipeline:
    def spider_opened(self, spider):
        self.coon = Redis(
            host='127.0.0.1',
            port=6379,
            db=2,
            decode_responses=True
        )

    def spider_closed(self, spider):
        if self.coon:
            self.coon.close()

    def process_item(self, item, spider):
        content = item['content']
        if content.coon.sismember("ty:pipline", content):
            print("已经有了")
        else:
            self.coon.sadd("ty:pipline", content)
            print("添加到新内容")
        return item
