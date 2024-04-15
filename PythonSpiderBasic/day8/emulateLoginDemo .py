import requests

url_login = "https://passport.17k.com/ck/user/login"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
#                   "Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"
# }
data = {
    "loginName": " 16538989670",
    "password": "q6035945",
}  # 樵夫老师的个人账号
resp = requests.post(url_login, data=data)
# print(resp.text)  # 登录成功

# 获取cookies
# print(resp.headers["Set-Cookie"])  # 字符串
# print(resp.cookies)  # requests-cookies
cookies17k = resp.cookies

# 获取书架信息
url_bookshelf = "https://user.17k.com/ck/author2/shelf?page=1&appKey=2406394919"
resp_bookshelf = requests.get(url_bookshelf, cookies=cookies17k)
# print(resp_bookshelf.text)

# 每个阶段的请求获取的cookies可能会不一样
