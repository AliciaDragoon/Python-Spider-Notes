from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import base64

# s = "这次转学结束后，我就要回老家和那女孩结婚了"
# # key的长度为8字节
# key = b"11111111"
# # aes = AES.new(key=key, mode=AES.MODE_ECB)
# # IV的长度应为8个字符
# iv = b"11111111"
# # print("iv:", iv)
# des = DES.new(key=key, mode=DES.MODE_CBC, IV=iv)
# bs = s.encode("utf-8")
# # 将bs填充到DES块大小的倍数
# bs = pad(bs, DES.block_size)
# result = des.encrypt(bs)
# print("result:", result)
# # result: b'\xc6\xfb\x95\xb6\n\x12\xde\x9dZ\x04,\xbf (\x15^\xed\x13\r\xf0\x9a\x07\xb0\x83\xe76$\x8e\x9a\xa0\x9e\xb4\xf4\xf0>\xd1\n\x9a\xefZ4\x97\xf4\x1a\xe5\x8e)\xe8?\x91\x8eQ\x0f\x03\xa9\xb0\xa4mu<qH \xda'

sec_dec_bs = b'\xc6\xfb\x95\xb6\n\x12\xde\x9dZ\x04,\xbf (\x15^\xed\x13\r\xf0\x9a\x07\xb0\x83\xe76$\x8e\x9a\xa0\x9e\xb4\xf4\xf0>\xd1\n\x9a\xefZ4\x97\xf4\x1a\xe5\x8e)\xe8?\x91\x8eQ\x0f\x03\xa9\xb0\xa4mu<qH \xda'
key = b"11111111"
iv = b"11111111"
des = DES.new(key, DES.MODE_CBC, iv)
bs = des.decrypt(sec_dec_bs)
bs = unpad(bs, 8)
print(bs.decode("utf-8"))
# 这次转学结束后，我就要回老家和那女孩结婚了
