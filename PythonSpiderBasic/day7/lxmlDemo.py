from lxml import etree

f = open("index.html", mode="r", encoding="utf-8")
content = f.read()  # 页面源代码

# 默认情况下，pycharm不知道类型，所以没有代码提示
page = etree.HTML(content)  # type: etree._Element
# page即读取到的页面源代码
# print(type(page))  # <class 'lxml.etree._Element'>
# 用type()得到数据类型，在变量被赋值位置添加# type: 类型

# root = page.xpath("/html")  # 筛选;"/"即html的根节点
# print(root)  # [<Element html at 0x12b1c9b2fc0>], 一个列表

# p = page.xpath("/html/body/div/p")
# print(p)
# p_text = page.xpath("/html/body/div/p/text()")  # text()可提取内部的文本
# print(p_text)  # ['个很厉害的人']
# p_text = page.xpath("/html/body/div/p//text()")  # "//"跳过子节点至孙节点

# divs = page.xpath("//div")  # 在整个页面搜索所有的div节点
# print(divs)
# divs_p = page.xpath("//div/p")  # 搜索后面带p节点的div节点
# print(divs_p)
# divs_p_text = page.xpath("//div/p/text()")
# print(divs_p_text)

# ol_ol_li_text = page.xpath("//ol/ol/li/text()")
# print(ol_ol_li_text)

# ol_ol_li_2_text = page.xpath("//ol/ol/li[2]/text()")  # xpath中可用[]数数，从1开始数，[2]即第二个
# print(ol_ol_li_2_text)

# li3rd = page.xpath("//li[3]/text()")
# print(li3rd)

# id_10086 = page.xpath("//li[@id= '10086']/text()")  # "@属性": 找特定属性值的键
# print(id_10086)

# "*": 单个任意标签
# cla = page.xpath("//*[@class]/text()")
# print(cla)

# 拿到所有href
# href1 = page.xpath("//ul/li/a/@href")
# print(href1)

# href_a_list = page.xpath("//ul/li/a")
# # print(href_a_list)
# for a in href_a_list:
#     # print(a)
#     href2 = a.xpath("./@href")[0]  # "./": 只在当前节点搜索
#     text = a.xpath("./text()")[0]
#     print(f"{text}: {href2}")

# 搜索倒数第一个
# last = page.xpath("//ol/li[last()]/a/@href")
# print(last)
# sTL = page.xpath("//ol/li[last()-1]/a/@href")
# print(sTL)
