# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
import pymongo

# 存储到文件
class CaiPipeline:
    # scrapy的open_spider函数会在爬虫开始时自动执行
    def open_spider(self, spider_name):
        self.f = open("data.csv", mode="w", encoding="utf-8")

    # scrapy的close_spider函数会在爬虫结束时自动执行
    def close_spider(self, spider_name):
        self.f.close()

    def process_item(self, item, spider):
        # print("管道", item["qi"], item["red_ball"], item["blue_ball"])
        self.f.write(item["qi"])
        self.f.write(",")
        self.f.write("_".join(item["red_ball"]))
        self.f.write(",")
        self.f.write(item["blue_ball"])
        self.f.write("\n")
        return item
        # return item 会将item传递到下一个管道


# 存储到MySql
class MySqlPipline:
    # 连接MySQL
    def open_spider(self, spider_name):
        self.coon = pymysql.connect(
            host="127.0.0.1",
            port=3306,
            database="cai",
            user="root",
            password="password"
        )

    # 关闭连接
    def close_spider(self, spider_name):
        self.coon.close()

    def process_item(self, item, spider):
        try:
            cur = self.coon.cursor()
            qi = item['qi']
            red_ball = "_".join(item['red_ball'])
            blue_ball = item['blue_ball']
            sql = f"insert into ssq(qi, red_ball, blue_ball) values('{qi}','{red_ball}','{blue_ball}')"
            cur.execute(sql)
            self.coon.commit()
        except Exception as e:
            print(e)
            # 出错的话回滚
            self.coon.rollback()
        return item


# 存储到MongoDB
class MongoPopline:
    def open_spider(self, spider_name):
        self.coon = pymongo.MongoClient(
            host= "127.0.0.1",
            port= 27017,
        )
        self.db = self.coon["localhost"]

    def close_spider(self, spider_name):
        self.coon.close()


    def process_item(self, item, spider):
        self.db.ssq.insert_one({"qi": item['qi'], "red_ball": item['red_ball'], "blue_ball": item['blue_ball']})
        return item
