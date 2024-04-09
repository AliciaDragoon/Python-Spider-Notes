# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


# 保存数据
class GamePipeline:
    def process_item(self, item, spider):
        # 引擎得到数据后，会判断数据类型，如果是数据，会自动调用pipline中的process_item函数
        print("我是pipline", item)
        # 默认下，pipline不工作，要在settings中开启
        return item
