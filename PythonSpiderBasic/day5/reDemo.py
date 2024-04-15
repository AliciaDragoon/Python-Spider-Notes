import re

# 结果 = re.findall(正则, 字符串) 找到所有，返回列表
# result = re.findall(r"\d+", "apple1000,dog1")  # r""可去除转义
# print(result)  # ['1000', '1']

# 结果 = re.finditer(正则, 字符串) 找到所有，返回迭代器。查找多个相同格式的结果
# result = re.finditer(r"\d+", "apple1000,dog1")
# print(result)  # <callable_iterator object at 0x00000212BFE21720>
# for it in result:
#     print(it)
#     <re.Match object; span=(5, 9), match='1000'>
#     <re.Match object; span=(13, 14), match='1'>
#     print(it.group())  # group()分组

# 全局搜索，搜索到了，返回第一个结果。查找单个相同格式的结果
# r = re.search(r"\d+", "apple1000,dog1")
# print(r)
# print(r.group())
#
# obj = re.compile(r"\d+")  # 加载正则表达式
# result = obj.finditer("apple1000,dog1")
# print(result)  # <callable_iterator object at 0x000001B8EAEF3AC0>

# 从json中获得想要的内容
# s = "start123end, start456end"
# obj = re.compile(r"start(?P<name>.*?)end")  # ():分组; ?P<name>: 给这一组起名
# result = obj.finditer(s)
# for item in result:
#     print(item.group("name"))  # 根据分组的名字提取具体数据

# re.sub(正则表达式，要替换的内容，要处理的字符串)