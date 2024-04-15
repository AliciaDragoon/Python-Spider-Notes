import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import EdgeOptions
from selenium.webdriver.common.action_chains import ActionChains

# 屏蔽webdriver特征
option = EdgeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
# 去掉自动化工具提示
option.add_argument("--disable-blink-features=AutomationControlled")
# 网站询问你是否自动化工具回答不是
web = webdriver.Edge(options=option)

web.maximize_window()
web.implicitly_wait(10)
web_url = "https://kyfw.12306.cn/otn/resources/login.html"
web.get(web_url)

username = "123456"
password = "123456"
web.find_element(By.ID, "J-userName").send_keys(username)
web.find_element(By.ID, "J-password").send_keys(password)
web.find_element(By.ID, "J-login").click()
time.sleep(2)

# 滑块处理
btn = web.find_elements(By.ID, 'nc_1_n1z')
# 按住滑块
ac = ActionChains(web).click_and_hold()
# 滑动300像素
ac.move_by_offset(xoffset=300, yoffset=0)
# 松手
ac.release()
ac.perform()

time.sleep(10)
