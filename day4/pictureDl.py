import requests

url = "https://img2.baidu.com/it/u=673003775,1191479950&fm=253&fmt=auto&app=138&f=JPEG?w=889&h=500"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299', }

resp = requests.get(url, headers=headers)
# print(resp)  # <Response [200]>
content = resp.content
# print(content)  # 获取的是字节
with open("picture1.jpg", mode='wb') as f:
    f.write(content)
