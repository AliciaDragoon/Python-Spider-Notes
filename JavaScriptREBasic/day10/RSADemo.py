# 公钥和私钥是一对
# 客户端拿到公钥，可以对数据加密
# 服务器使用私钥计算出公钥，解密数据

# 加密器
from Crypto.Cipher import PKCS1_v1_5
# 生成密钥
from Crypto.PublicKey import RSA

import base64

rsa_key = RSA.generate(1024)
# 打印私钥
print(rsa_key.export_key().decode())
# PEM格式

# print(rsa_key.export_key(format="DER"))
# 字节

# print(base64.b64encode(rsa_key.export_key(format="DER")))

# 使用私钥计算出公钥
rsa_public_key = rsa_key.publickey()
print(rsa_public_key.export_key().decode())
# PEM格式
