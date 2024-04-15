from selenium import webdriver

web = webdriver.Edge()
web.maximize_window()  # 窗口最大化
web.get("https://www.baidu.com/")
print(web.title)
