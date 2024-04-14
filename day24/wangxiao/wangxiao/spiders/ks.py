import json

import scrapy


class KsSpider(scrapy.Spider):
    name = "ks"
    allowed_domains = ["wangxiao.cn"]
    start_urls = ["http://ks.wangxiao.cn"]

    def parse(self, resp, **kwargs):
        # print(resp.url)
        # 解析页面结构
        li_list = resp.xpath("//ul[@class='first-title']/li")
        for li in li_list:
            first_title = li.xpath("./p/span/text()").extract_first()
            # print(first_title)
            a_list = li.xpath("./div/a")
            for a in a_list:
                second_title = a.xpath("./text()").extract_first()
                second_url = a.xpath("./@href").extract_first()
                second_url = resp.urljoin(second_url)
                # 模拟考试
                second_url = second_url.replace("TestPaper", "exampoint")
                # 考点练习
                # print(first_title, second_title, second_url)
                yield scrapy.Request(
                    # url=second_url,
                    callback=self.parse_second,
                    # meta={'first_title': first_title, 'second_title': second_title},
                    # 测试
                    url="http://ks.wangxiao.cn/exampoint/list?sign=jz1",
                    meta={'first_title': "工程类", 'second_title': "一级建造师"}
                )
                # 中断parse()
                return

    def parse_second(self, resp, **kwargs):
        first_title = resp.meta['first_title']
        second_title = resp.meta['second_title']
        # print(first_title, second_title, resp.url)
        a_list = resp.xpath("//div[@class='filter-item']/a")
        for a in a_list:
            third_title = a.xpath("./text()").extract_first()
            third_url = a.xpath("./@href").extract_first()
            third_url = resp.urljoin(third_url)
            # print(third_title, third_url)
            yield scrapy.Request(
                callback=self.parse_third,
                url=third_url,
                meta={'first_title': first_title, 'second_title': second_title, 'third_title': third_title}

            )
            return

    def parse_third(self, resp, **kwargs):
        first_title = resp.meta['first_title']
        second_title = resp.meta['second_title']
        third_title = resp.meta['third_title']
        # print(first_title, second_title, third_title, resp.url)
        # 每个章节的结构都不一样，从内向外溯源
        chapter_items = resp.xpath("//div[@class='panel-content']/ul[@class='chapter-item']")
        for chapter_item in chapter_items:
            section_point_item = chapter_item.xpath(".//ul[@class='section-point-item']")
            # 有子ul，就是文件夹；没有就是文件
            if section_point_item:
                # section_point_item是最里层
                for point_item in section_point_item:
                    # 从最内层向外查找元素
                    points = point_item.xpath("./ancestor::ul[@class='chapter-item' or @class='section-item']")
                    r = [first_title, second_title, third_title]
                    for point in points:
                        p_name = "".join(point.xpath("./li[1]//text()").extract()).strip().replace(' ', '')
                        # 文件夹
                        r.append(p_name)
                    file_path = "/".join(r)
                    # print(file_path)
                    file_name = "".join(point_item.xpath("./li[1]//text()").extract()).strip().replace(' ', '')
                    # print(file_path, file_name)
                    top = point_item.xpath("./li[2]/text()").extract_first().split('/')[1]
                    # print(top)
                    sign = point_item.xpath("./li[3]/span/@data_sign").extract_first()
                    subsign = point_item.xpath("./li[3]/span/@data_subsign").extract_first()
                    data = {
                        "examPointType": "",
                        "practiceType": "2",
                        "questionType": "",
                        "sign": sign,
                        "subsign": subsign,
                        "top": top,
                    }
                    # 发送请求到listQuestions获取题目
                    url = "http://ks.wangxiao.cn/practice/listQuestions"
                    yield scrapy.Request(
                        url=url,
                        method="post",
                        body=json.dumps(data),
                        headers={'Content-Type': 'application/json;charset=UTF-8'},
                        callback=self.parse_Questions,
                        meta={
                            "file_path": file_path,
                            "file_name": file_name
                        }
                    )
                    return
            else:
                file_path = "/".join([first_title, second_title, third_title])
                file_name = "".join(chapter_item.xpath("./li[1]//text()").extract()).strip().replace(' ', '')
                top = chapter_item.xpath("./li[2]/text()").extract_first().split('/')[1]
                # print(top)
                sign = chapter_item.xpath("./li[3]/span/@data_sign").extract_first()
                subsign = chapter_item.xpath("./li[3]/span/@data_subsign").extract_first()
                data = {
                    "examPointType": "",
                    "practiceType": "2",
                    "questionType": "",
                    "sign": sign,
                    "subsign": subsign,
                    "top": top,
                }
                # 发送请求到listQuestions获取题目
                url = "http://ks.wangxiao.cn/practice/listQuestions"
                yield scrapy.Request(
                    url=url,
                    method="post",
                    body=json.dumps(data),
                    headers={'Content-Type': 'application/json;charset=UTF-8'},
                    callback=self.parse_Questions,
                    meta={
                        "file_path": file_path,
                        "file_name": file_name
                    }
                )
                return

    def parse_Questions(self, resp, **kwargs):
        file_path = resp.meta['file_path']
        file_name = resp.meta['file_name']
        print(resp.text)
