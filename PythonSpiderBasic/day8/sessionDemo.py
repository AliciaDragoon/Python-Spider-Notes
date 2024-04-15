import requests

session = requests.session()  # 可以自动保持会话（自动更新cookies）
session.headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                  "Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"
}  # 使用session设置头文件

# session.cookies = {}  # 使用session设置cookies

url_login = "https://passport.17k.com/ck/user/login"
data = {
    "loginName": " 16538989670",
    "password": "q6035945",
}

resp = session.post(url_login, data=data)
# print(resp.text)  # session会将响应获取到的cookies更新到session，后续的请求都会有cookies
url_bookshelf = "https://user.17k.com/ck/author2/shelf?page=1&appKey=2406394919"
resp_bookshelf = session.get(url_bookshelf)
# print(resp_bookshelf.text)
# session对js无效
