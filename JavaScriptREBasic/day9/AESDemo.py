# 对称加密
# 加密和解密时使用相同的密钥
# 常见的对称加密算法有AES，DES，3DES
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64

s = "这次转学结束后，我就要回老家和那女孩结婚了"
# key的长度至少16字节
key = b"1111111111111111"
# AES.MODE_ECB没有使用初始化向量（IV），并且相同的明文块会产生相同的密文块
# aes = AES.new(key=key, mode=AES.MODE_ECB)
iv = os.urandom(16)
aes = AES.new(key=key, mode=AES.MODE_CBC, IV=iv)
bs = s.encode("utf-8")
# 将bs填充到AES块大小的倍数
bs = pad(bs, AES.block_size)
result = aes.encrypt(bs)
# print(result)

# sec_ecb_bs = b'\x7f\xdd\xf2\xa8\xd1\x07\xaas\xa1AB{\xdd\x91\x05\xd69r\xbf\xea\xe5`\xd4\xd9\xe6\x12\xf64>\xf1\xe3L\xda}\xe5\xb3oY\x1bc\xe5W,\xa7\xf2\xf0\xf6t\xa0\xfd\xc7\xed#eU\xc9\xa4\xec(o.\x1f(\xf0'
sec_cbc_bs = b"\x17e\xf4\xc1?g'\x8d\x03\xd6(?{\xc3a\xa4B\n\x94\xb8p`\xffuJl\xb6\xac\xa8\x06\xbe\xcc\xca\xc4e\xa5\xb6\x92\xe8h\xd7d\x95B\r\x19\xa5fp~\x1b\x81K\xa5\xc0\xef0]1\x15\x95\xd34\xf3"
# 被加密的数据不能用utf-8或gbk处理
bs64 = base64.b64encode(sec_cbc_bs).decode()
# print(bs64)
# F2X0wT9nJ40D1ig/e8NhpEIKlLhwYP91Smy2rKgGvszKxGWltpLoaNdklUINGaVmcH4bgUulwO8wXTEVldM08w==
# 前端接收到的就是这样的数据

