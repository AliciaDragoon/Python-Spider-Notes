import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 "
                  "Safari/537.36 Edg/122.0.0.0"
}


def get_proxy():
    ip_api_url = "http://127.0.0.1:5800/get_proxy"
    resp = requests.get(url, headers=headers)
    dic = resp.json()
    proxy = {
        "http": "http://"+dic['ip'],
        # "https": "https://"+dic['ip'],
        "https": "http://" + dic['ip'],
    }
    return proxy


url = "http://www.baidu.com/s?wd=ip"
resp = requests.get(url, proxies=get_proxy(), headers=headers)
print(resp.text)
