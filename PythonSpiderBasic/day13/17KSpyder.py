# selenium登录，获取cookies，requests爬取
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import EdgeOptions
from selenium.webdriver.common.action_chains import ActionChains
import requests

# 屏蔽webdriver特征
option = EdgeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
# 去掉自动化工具提示
option.add_argument("--disable-blink-features=AutomationControlled")
# 网站询问你是否自动化工具回答不是
web = webdriver.Edge(options=option)

web.maximize_window()
web.implicitly_wait(10)
web_url = "https://www.17k.com/"
web.get(web_url)

username = "16538989670"
password = "q6035945"

web.find_element(By.XPATH, "//*[@id='header_login_user']/a[1]").click()
# 登录弹窗在iframe中
iframe = web.find_element(By.XPATH, "/html/body/div[21]/div/div[1]/iframe")
web.switch_to.frame(iframe)
# 切换到iframe中

# 登录
time.sleep(1)
web.find_element(By.XPATH, "/html/body/form/dl/dd[2]/input").send_keys(username)
web.find_element(By.XPATH, "/html/body/form/dl/dd[3]/input").send_keys(password)
web.find_element(By.XPATH, "//*[@id='protocol']").click()
web.find_element(By.XPATH, "/html/body/form/dl/dd[5]/input").click()
time.sleep(5)

# 记录cookies
cookies = web.get_cookies()
# print(cookies)

# 转换cookies
cookie = {}
for item in cookies:
    name = item['name']
    value = item['value']
    cookie[name] = value

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 "
                  "Safari/537.36 Edg/122.0.0.0"
}

resp = requests.get("https://user.17k.com/ck/author2/shelf?page=1&appKey=2406394919", headers=headers, cookies=cookie)
print(resp.text)
