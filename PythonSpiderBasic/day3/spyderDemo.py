from urllib.request import urlopen

url = "http://www.baidu.com/"
resp = urlopen(url)
result = resp.read()
print(result)