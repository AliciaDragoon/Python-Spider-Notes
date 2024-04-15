# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os
from scrapy.pipelines.images import ImagesPipeline
from lxml import etree
import scrapy


class WangxiaoPipeline:
    # 保存到md文件中，既能保留页面格式，又能保存图片（re.sub可以去除HTML标签）
    def process_item(self, item, spider):
        # print(item)
        file_name = item['file_name']
        file_path = item['file_path']
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        real_file_path = file_path + "/" + file_name + ".md"
        with open(real_file_path, mode="a", encoding="utf-8") as f:
            f.write(item['question_info'])
            f.write("\n")
            f.write("\n")
        return item


# 下载题目中的图片
class WangxiaoImagePipeline(ImagesPipeline):
    # 发送下载请求
    def get_media_requests(self, item, info):
        # 获取图片下载链接
        tree = etree.HTML(item["question_info"])
        srcs = tree.xpath('//image/@src')
        for src in srcs:
            yield scrapy.Request(
                url=src,
                dont_filter=True,
                meta={
                    "src": src,
                    # 防止重定向，传递src
                    "file_name": item["file_name"],
                    "file_path": item["file_path"],
                }
            )

    # 下载路径
    def file_path(self, request, response=None, info=None, *, item=None):
        src = request.meta["src"]
        file_path = request.meta["file_path"]
        file_name = request.meta["file_name"]
        real_file_name = src.rsplit("/")[-1]
        real_file_path = file_path + "/" + file_name + "_imgs2" + "/" + real_file_name
        return real_file_path

    # 把md中的图片下载路径替换为本地图片路径
    def item_completed(self, results, item, info):
        # print(results)
        for r in results:
            status = r[0]
            dic = r[1]
            # 如果下载成功
            if status:
                src = dic["url"]
                path = dic["path"]
                # 绝对路径
                rp_list = path.split("/")[-2:]
                real_path = rp_list[0] + "/" + rp_list[1]
                # 相对路径
                item["question_info"] = item["question_info"].replace(src, real_path)
        return item
