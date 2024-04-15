import requests

headers = {
    "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 "
        "Safari/537.36 Edg/120.0.0.0",
}

dic = {
    "http": "http://223.96.90.216:8085",
    "https": "https://223.96.90.216:8085",
}  # TimeoutError: [WinError 10060]

url = "https://ip.900cha.com/"

resp1 = requests.get(url, proxies=dic, headers=headers)
print(resp1.text)
resp2 = requests.get(url, headers=headers)
print(resp2.text)