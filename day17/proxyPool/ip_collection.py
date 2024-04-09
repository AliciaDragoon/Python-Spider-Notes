# 采集代理ip
from proxy_redis import ProxyRedis
import requests
import re
import json
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 "
                  "Safari/537.36 Edg/122.0.0.0"
}

# 获取快代理的普通开放代理
def get_kua_ip(red):
    url = "https://www.kuaidaili.com/free/intr/"
    resp = requests.get(url, headers=headers)
    # newbing写的获取ip_port的代码
    page_content = resp.text
    pattern = r"const fpsList = (\[.*?\]);"
    match = re.search(pattern, page_content)
    if match:
        fps_list_content = match.group(1)
        # print(type(fps_list_content))
    converted_list = json.loads(fps_list_content)
    # print(type(converted_list))
    # print(converted_list)
    ip_port_list = [f"{item['ip']}:{item['port']}" for item in converted_list]
    # print(ip_port_list)

    for ip_port in ip_port_list:
        # print(ip_port)
        red.add_proxy_ip(ip_port)

# 更多免费代理ip网站可以私信newbing
# def get_another_daili_ip():
#     url = ""
#     resp = requests.get(url, headers=headers)
#     '''
#     爬取ip:port
#     '''
#     for ip_port in ip_port_list:
#         # print(ip_port)
#         red.add_proxy_ip(ip_port)

def run():
    # 创建red存储
    red = ProxyRedis()
    # 每分钟循环一次
    while 1:
        # 采集快代理
        try:
            get_kua_ip(red)
            # 采集其他代理网站
            # get_another_daili_ip(red)
        except:
            print("采集遇到错误")
        time.sleep(60)


if __name__ == '__main__':
    run()
    # 把启动功能单独封装，方便采用多线程运行