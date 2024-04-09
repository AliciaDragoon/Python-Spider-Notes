# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline


class TuPipeline:
    def process_item(self, item, spider):
        # print(item["img_src"])
        return item


# scrapy的图片视频下载方法
class TuImagesPipeline(ImagesPipeline):
    # 发送下载图片的请求
    def get_media_requests(self, item, info):
        url = item["img_src"]
        yield scrapy.Request(url=url)

    # 图片下载到路径
    def file_path(self, request, response=None, info=None, *, item=None):
        # 设置文件路径
        img_file_path = "dongman/1"
        # 设置文件名
        file_name = item["img_src"].split("/")[-1]
        # 拼接路径和文件名
        img_path = img_file_path + "/" + file_name
        return img_path

    # 更新item
    def item_completed(self, results, item, info):
        print(results)
        return item
