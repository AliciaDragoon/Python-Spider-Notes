import requests
import json

# Payload:Form data不放入url
# 抓包时获取url,data,post(F12,networks,fetch/xhr,payload)
url = "https://fanyi.baidu.com/sug"

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/78.0.3904.97 Safari/537.36'}

requests.post(url)

# 准备参数
data = {
    "kw": "jay"
}  # Form data放入data

resp = requests.post(url, data=data, headers=headers)
# print(resp.text)

# 方案1
# dic = json.loads(resp.text)
# print(dic)

# 方案2，能直接把返回的内容处理成json
dic = resp.json()
# 服务器返回的内容是json才能用这种方案
# print(resp.text)  # 获取的是字符串

print(resp.json())  # 获取的是字典
print(dic)