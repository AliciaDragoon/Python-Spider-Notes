# 下载中大网校全科目考点练习中的题目
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
                    url=second_url,
                    callback=self.parse_second,
                    meta={'first_title': first_title, 'second_title': second_title},
                    # 测试
                    # url="http://ks.wangxiao.cn/exampoint/list?sign=jz1",
                    # meta={'first_title': "工程类", 'second_title': "一级建造师"}
                )
                # 中断parse()
                # return

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
            # return

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
                        callback=self.parse_questions,
                        meta={
                            "file_path": file_path,
                            "file_name": file_name
                        }
                    )
                    # return
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
                    callback=self.parse_questions,
                    meta={
                        "file_path": file_path,
                        "file_name": file_name
                    }
                )
                # return

    def parse_questions(self, resp, **kwargs):
        file_path = resp.meta['file_path']
        file_name = resp.meta['file_name']
        # print(type(resp))
        dic = resp.json()
        # print(type(dic))
        data_list = dic['Data']
        # print(data_list)
        for data in data_list:
            questions = data['questions']
            # 仔细观察，多多尝试
            if questions:
                # 拿到每一道选择题，单选，多选，判断
                for question in questions:
                    question_info = self.process_question(question)
                    yield {
                        "file_path": file_path,
                        "file_name": file_name,
                        "question_info": question_info
                    }
            else:
                # 拿到材料题
                materials = data.get('materials')
                for mater in materials:
                    # 获取材料内容
                    mater_content = mater['material']['content']
                    questions = mater['questions']
                    qs = []
                    for question in questions:
                        question_info = self.process_question(question)
                        qs.append(question_info)
                    # 拼接材料和题目
                    mater_content = mater_content + "\n\n" + "\n".join(qs)
                    yield {
                            "file_path": file_path,
                            "file_name": file_name,
                            "question_info": mater_content
                    }

    # 题目处理
    def process_question(self, question):
        # 获取题目
        content = question['content']
        # 获取选项
        options = question['options']
        right_list = []
        options_list = []
        for option in options:
            # 获取选项的序号，内容，正确与否
            option_name = option["name"]
            option_content = option["content"]
            # 拼接选项的序号和内容
            option_str = option_name + ":" + option_content
            options_list.append(option_str)
            option_isright = option["isRight"]
            if option_isright == 1:
                # 如果答案正确
                # 区分选择题和判断题
                if option_name in "ABCDEFGHIJKLMNO":
                    right_list.append(option_name)
                else:
                    right_list.append(option_content)
        # 获取题目解析
        analysis = question['textAnalysis']
        # 拼接题目，选项，答案和解析
        if right_list:
            question_info = (content + "\n"
                             + "\n".join(options_list) + "\n\n"
                             + "答案：" + "\n" + "，".join(right_list) + "\n"
                             + "解析：" + analysis)
        else:
            # 简述题只有解析没有答案
            question_info = (content + "\n"
                             + "\n".join(options_list) + "\n\n"
                             + "解析：" + analysis)
        return question_info
