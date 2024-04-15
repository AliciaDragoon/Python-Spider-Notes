import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import base64
import json
import requests


def base64_api(uname, pwd, img, typeid):
    data = {"username": uname, "password": pwd, "typeid": typeid, "image": img}
    # 直接放入base64格式的img
    result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        return result["message"]


web = webdriver.Edge()
web.get("https://www.bilibili.com/")
# 软等待
web.implicitly_wait(10)
username = "username"
password = "password"
# 点击登录按钮
web.find_element(By.CLASS_NAME, "header-login-entry").click()
# 在弹窗中输入用户名和密码
web.find_elements(By.XPATH, "//*[@class='form__item']/input")[0].send_keys(username)
web.find_elements(By.XPATH, "//*[@class='form__item']/input")[1].send_keys(password)

web.find_element(By.CLASS_NAME, "btn_primary ").click()

# 获取验证码窗口截图
pic = web.find_elements(By.CLASS_NAME, "geetest_widget")[0]
time.sleep(10)
pic.screenshot("pic.png")

# 用图鉴识别验证码
username = "q6035945"
password = "q6035945"
verify_code = base64_api(username, password, "pic.png", 27)
# print(verify_code)
# 返回字符的坐标(11,11|22,22|33,33)

# 根据字符坐标，依次模拟鼠标点击
verify_code = verify_code.split("|")
for codes in verify_code:
    x, y = codes.split(",")
    x = int(x)
    y = int(y)
    # 事件链（动作链）
    ActionChains(web).move_to_element_with_offset(pic, xoffset=x, yoffset=y).click().perform()
    time.sleep(2)
time.sleep(2)

# 点击确认提交验证码
web.find_elements(By.CLASS_NAME, "geetest_commit_tip")[2].click()

time.sleep(10)
