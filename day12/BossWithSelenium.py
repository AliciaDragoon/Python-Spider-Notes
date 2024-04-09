from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

web = webdriver.Edge()
web.get("https://www.zhipin.com/beijing/")

# 使用 XPath 定位找到搜索栏
input_el = web.find_element(By.XPATH, '//*[@id="wrap"]/div[3]/div/div[1]/div[1]/form/div[2]/p/input')


# 输入python并回车
input_el.send_keys("python", Keys.ENTER)
# time.sleep(10)
# 浏览器加载慢可能会导致没找到会报错

# 获取当前页面的所有职位
li_list = web.find_elements(By.XPATH, "//div[@class='search-job-result']/ul/li")
# 类似bs4.find_all
# print(len(li_list))
# 30

for li in li_list:
    span_element = li.find_element(By.CLASS_NAME, 'job-name')
    # 在selenium的xpath中，最后一项不能是@xxx或text()
    # job_title = span_element.text
    # print(job_title)
    # link = li.find_element(By.CLASS_NAME, 'job-card-left').get_attribute('href')
    # price = li.find_element(By.CLASS_NAME, 'salary')
    # print(job_title, link, price.text)

    # 模拟点击职位
    span_element.click()
    time.sleep(10)
    # 切换到新弹出的页面
    web.switch_to.window(web.window_handles[-1])
    # 获取职位详情
    job_details = web.find_element(By.XPATH,"//div[@class='job-detail']").text
    print(job_details)
    print("=======")
    # 关闭职位页面窗口
    web.close()
    # 切换回之前的窗口
    web.switch_to.window(web.window_handles[0])
    # break
