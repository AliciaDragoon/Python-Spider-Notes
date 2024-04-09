# 使用selenium切换iframe
from selenium import webdriver
from selenium.webdriver.common.by import By

web = webdriver.Edge()

url = "wbdy.tv/play/69328_1_1.html"

web.get(url)

iframe = web.find_element(By.XPATH, "//iframe[@id='mplay']")

# 切入iframe，以提取iframe中的内容
web.switch_to.frame(iframe)
video = web.find_element(By.XPATH, "//video")

# 获取视频播放链接
src = video.get_property("src")
print(src)

# 切换回上一层frame
web.switch_to.parent_frame()

web.close()
