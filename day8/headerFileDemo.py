import requests

url = "https://user.17k.com/ck/author2/shelf?page=1&appKey=2406394919"
headers = {
    "Cookie": "GUID=88190ba9-3b22-4c62-bc34-2ec896276b2b; "
              "accessToken=nickname%3D%25E4%25B9%25A6%25E5%258F%258Bc3ueyT296%26avatarUrl%3Dhttps%253A%252F%252Fcdn"
              ".static"
              ".17k.com%252Fuser%252Favatar%252F06%252F26%252F88%252F102708826.jpg-88x88%253Fv%253D1702729100165%26id"
              "%3D102708826%26e%3D1718281103%26s%3D638814f1c3c676f0; c_channel=0; c_csc=web",
    # 放入经验证的cookies（从浏览器端复制一个）
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                  "Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"}
# 该头文件只对老网站有效

resp = requests.get(url, headers=headers)
print(resp.text)
