# 公钥和私钥是一对
# 客户端拿到公钥，可以对数据加密
# 服务器使用私钥计算出公钥，解密数据

# 加密器
from Crypto.Cipher import PKCS1_v1_5
# 生成密钥
from Crypto.PublicKey import RSA

import base64

# rsa_key = RSA.generate(1024)
# # 打印私钥
# print(rsa_key.export_key().decode())
# # PEM格式
#
# # print(rsa_key.export_key(format="DER"))
# # 字节
#
# # print(base64.b64encode(rsa_key.export_key(format="DER")))
#
# # 使用私钥计算出公钥
# rsa_public_key = rsa_key.publickey()
# print(rsa_public_key.export_key().decode())
# # PEM格式

# 常规的生成密钥的逻辑
# 一般会在每天早上两点或者服务器启动的时候生成一对密钥，而不是给每个用户生成一对密钥
# rsa_key = RSA.generate(2048)
# with open('rsa_private_key.pem', 'wb') as f:
#     f.write(rsa_key.exportKey())
#
# with open('rsa_public_key.pem', 'wb') as f:
#     f.write(rsa_key.public_key().exportKey())

# s = "东京皇帝☆北条恋歌"
#
# # 使用公钥加密
# f = open("rsa_public_key.pem", "rb")
# public_key_bytes = f.read()
# # 加载公钥
# public_key = RSA.importKey(public_key_bytes)
# f.close()
# # 创建加密器
# cipher = PKCS1_v1_5.new(public_key)
# # 得到密文
# ciphertext = cipher.encrypt(s.encode("utf-8"))
# # print(ciphertext)

# 解密
ciphertext = b"y\x01T\xac\x8a!|\xba\x1bo\xc5\x14\x95\x94&9\xd4&7\x87\x9c\xb3m\x1ek5\n\xe9\x8c\x86\\H\xba\xeb\xcb\xb7\xc1,\xf4\xc1^\xc9B\xb8\xcb\xe0\xec;0\xb9\x1a0V\xd7:\x03e>\x07\xfa\xd9\x00\x86\xb1I\xab*\xa2e\x14\x88\x16\xfbr\xd9P|\xc6\x97\xce\xb5>\xc3\x0bZ\xab#\xef\xd8\xfa\xf2+\xe3\xd0\xfb\xcc\x10\xc0\xa5\x15\xcd\x9b\x1a\xc6La\xd5\x99K4\xf4v\x1a \xcbd\x130\xdf\x9e\xc3\xa3]\x11\xaa:\x04\xefo`\xf3mM\x83h&\xd3C\xd8%^9\\\x8a5\x18u3%e\x87\xa4U\xc4\xad\x94\x84y\xed!\x9c\x8e\n\x12j\xc4cr\xe2k\x16\x1c\xe8\xb7M\xc9\xa6Nu\xadN\xa5\x96\x9fv\xe0D\xb4hx\xde-\x9b\x8a\xc8a\x05ixB^\xf4\xf1g\xe9;q\x0e\x06\x958\xe1\x9a\xee\x1b\x0f\x1d\xa0\x0f\xe1\xb4\xbf\xa0\xa4!9$>\x01\x1e\x9e\xd9o\xba\xa04\xa6+\x11\xfa\xed\x02*\xca'\x1f\xbfP\x15T\x10z\xbc9\xe7c"
# 读取私钥
f = open("rsa_private_key.pem", "rb")
private_key = RSA.importKey(f.read())
f.close()
# 创建解密对象
plain = PKCS1_v1_5.new(private_key)
plaintext = plain.decrypt(ciphertext, None)
print(plaintext.decode("utf-8"))
# 东京皇帝☆北条恋歌
