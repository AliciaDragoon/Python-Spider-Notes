# http协议传输的数据包：
# 请求行 url 请求方式 http版本
# 请求头 ua cookie content-type xml referer
#
# 请求体 get/post
import base64

# http协议擅长处理字符串，不擅长字节
# 网站常常加密传输的数据

# base64可以把字节转换成字符串，每3个字节转换成4个字符

# s = "魔法泽茜"
# bs = s.encode("utf-8")
# print(bs)
# # b'\xe9\xad\x94\xe6\xb3\x95\xe6\xb3\xbd\xe8\x8c\x9c'
#
# # 把字节编码成b64字符串
# b64_s = base64.b64encode(bs)
# print(b64_s)
# # b'6a2U5rOV5rO96Iyc'
# b64_s = b64_s.decode("utf-8")
# print(b64_s)
# # 6a2U5rOV5rO96Iyc

# 把b64字符串编码成字节
s = "6a2U5rOV5rO96Iyc"
bs = base64.b64decode(s)
print(bs)
# b64字符串本质是字节
