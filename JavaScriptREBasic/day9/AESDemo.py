# 对称加密
# 加密和解密时使用相同的密钥
# 常见的对称加密算法有AES，DES，3DES

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

# s = "这次转学结束后，我就要回老家和那女孩结婚了"
# # key的长度至少16字节
# key = b"1111111111111111"
# # AES.MODE_ECB没有使用初始化向量（IV），并且相同的明文块会产生相同的密文块
# # aes = AES.new(key=key, mode=AES.MODE_ECB)
# IV的长度应为16个字符
# iv = b"1111111111111111"
# print("iv:", iv)
# aes = AES.new(key=key, mode=AES.MODE_CBC, IV=iv)
# bs = s.encode("utf-8")
# # 将bs填充到AES块大小的倍数
# bs = pad(bs, AES.block_size)
# result = aes.encrypt(bs)
# print("result:", result)
# # sec_ecb_bs = b""
# # sec_cbc_bs = b"R\x05\x8d\xa3\x94\xe3\x80\xacjF^\xd9'\xc4\xabgJ\xc9\xba\x88e\x87|\xccL\x84Q6\xd2\x8a\xcce\xf7\xb1\x9e/\xcdE\xdd\x9f\xce\x89\xa3\xfc\xbbqK\xcc=P\xb0\xbc<\x91\xf0\x0cH\xde\xdb \xcd\xf7x["
# # 被加密的数据不能用utf-8或gbk处理
# bs64 = base64.b64encode(result).decode()
# print("bs64:", bs64)
# # UgWNo5TjgKxqRl7ZJ8SrZ0rJuohlh3zMTIRRNtKKzGX3sZ4vzUXdn86Jo/y7cUvMPVCwvDyR8AxI3tsgzfd4Ww==
# # 前端接收到的就是这样的数据

# 解密
ss = "UgWNo5TjgKxqRl7ZJ8SrZ0rJuohlh3zMTIRRNtKKzGX3sZ4vzUXdn86Jo/y7cUvMPVCwvDyR8AxI3tsgzfd4Ww=="
key = b"1111111111111111"
iv = b"1111111111111111"

aes = AES.new(key, AES.MODE_CBC, iv)
# 把b64处理为字节
b6s_ss = base64.b64decode(ss)

bs = aes.decrypt(b6s_ss)
# print(bs)
# b'\xe8\xbf\x99\xe6\xac\xa1\xe8\xbd\xac\xe5\xad\xa6\xe7\xbb\x93\xe6\x9d\x9f\xe5\x90\x8e\xef\xbc\x8c\xe6\x88\x91\xe5\xb0\xb1\xe8\xa6\x81\xe5\x9b\x9e\xe8\x80\x81\xe5\xae\xb6\xe5\x92\x8c\xe9\x82\xa3\xe5\xa5\xb3\xe5\xad\xa9\xe7\xbb\x93\xe5\xa9\x9a\xe4\xba\x86\x01'
# bs是解密后的字节，经过填充
bs = unpad(bs, AES.block_size)
print(bs.decode("utf-8"))
# 这次转学结束后，我就要回老家和那女孩结婚了
