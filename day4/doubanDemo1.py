import requests

# url = "https://movie.douban.com/typerank?type_name=%E7%88%B1%E6%83%85&type=13&interval_id=100:90&action="
# 首先观察想要的东西在不在页面源代码，
# 如果在，直接请求页面源代码
# 如果不在，抓包观察数据是从哪个url加载进来的
url = "https://movie.douban.com/j/chart/top_list?type=13&interval_id=100%3A90&action=&start=0&limit=20"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/78.0.3904.97 Safari/537.36'}
resp = requests.get(url, headers=headers)
# print(resp.json())  # requests.exceptions.JSONDecodeError
# 说明返回的不是json

# print(resp.text)
# 返回空内容，说明被反爬了，添加ua

dic = resp.json()
print(dic)

# payload中有五个参数，参数较少时尚可采用本方案
