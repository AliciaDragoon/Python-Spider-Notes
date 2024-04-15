import json
import requests

# url = "https://movie.douban.com/j/chart/top_list"
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) '
#                          'Chrome/78.0.3904.97 Safari/537.36'}

# dic = {
#     "type": "13",
#     "interval_id": "100:90",
#     "action": "",
#     "start": "0",  # 0是第一页，20是第二页，40是第三页，以此类推
#     "limit": "20"
# }
# # 发送带参数的get请求，使用params传参
# resp = requests.get(url, params=dic, headers=headers)
# print(resp.json())
# # print(resp.request.url)

for i in range(5):
    start = i * 20
    url = "https://movie.douban.com/j/chart/top_list"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) '
               'Chrome/78.0.3904.97 Safari/537.36'}
    dic = {
        "type": "13",
        "interval_id": "100:90",
        "action": "",
        "start": start,
        "limit": "20"
    }
    # print(dic)
    resp = requests.get(url, params=dic, headers=headers)
    print(resp.json())
    # print(type(resp.json()))