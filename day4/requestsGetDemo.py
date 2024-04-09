import requests

content = input("请输入一个关键字：")
url = f"https://www.sogou.com/web?query={content}"

# 伪装成Safari浏览器
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/78.0.3904.97 Safari/537.36'}
# 发送get请求
resp = requests.get(url, headers=headers)

# requests.post() #发送post请求
# print(resp)  # <Response [200]>


# 获取响应体的内容（页面源代码）
page_source = resp.text
print(page_source)
# 响应.请求.请求头（UA）
print(resp.request.headers)

# Payload:Query String parameters放入url
