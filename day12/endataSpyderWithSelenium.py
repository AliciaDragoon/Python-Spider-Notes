# 先写有界面的，再考虑无头浏览器

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
# 可用于处理下拉框

import time
from selenium.webdriver.edge.options import Options

# 创建浏览器参数
opt = Options()
opt.add_argument("--headless") # 无头浏览器
opt.add_argument("--disable-gpu") # 禁用GPU加速
opt.add_argument("--window-size=4000,1600") # 设置窗口大小，确保所有元素都在可见范围内

#创建浏览器
web = webdriver.Edge(options=opt)
url = "https://www.endata.com.cn/BoxOffice/BO/Year/index.html"
web.get(url)

# 爬取当前页面
TableList = web.find_element(By.ID, "TableList")
# print(TableList.text)

# 切换年份选项
# 下拉菜单是select
sel = web.find_element(By.ID, "OptionDate")
# 获取菜单的每个选项
sel = Select(sel)
for option in sel.options:
    o = option.text
    sel.select_by_visible_text(o)
    # 获取每个选项的文本
    time.sleep(2)
    TableList = web.find_element(By.ID, "TableList")
    print(TableList.text)
    break


