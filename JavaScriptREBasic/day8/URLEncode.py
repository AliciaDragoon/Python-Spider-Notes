# 为了防止参数中的特殊符号引发歧义，浏览器会自动对请求的url进行编码，把参数转化为字节，每字节再转化为2个16进制数字，以%开头
from urllib.parse import urljoin, urlencode, quote, unquote

# dic = {
#     "name": "AliciaDragoon",
#     "age": 700,
#     "city": "旗谷学园 冒险寮",
# }
# r = urlencode(dic)
# print(r)
# # name=AliciaDragoon&age=700&city=%E6%97%97%E8%B0%B7%E5%AD%A6%E5%9B%AD+%E5%86%92%E9%99%A9%E5%AF%AE
# # requests.get(url, params=dic)

# s = "旗立飒太"
# ss = quote(s)
# print(s, ss)
# 旗立飒太 %E6%97%97%E7%AB%8B%E9%A3%92%E5%A4%AA

# 逆向时url和参数不需要手工处理，cookies需要手工处理，剔除特殊符号

# s = "%E6%97%97%E7%AB%8B%E9%A3%92%E5%A4%AA"
# print(unquote(s))
# 也可以通过在线工具转换
