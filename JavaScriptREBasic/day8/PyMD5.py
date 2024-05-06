from hashlib import md5

obj = md5()

# MD5的对象需为字节
name = "AliciaDragoon".encode('utf-8')

obj.update(name)
val = obj.hexdigest()
print(val, len(val))
# d89714bdeedd1e16de1ac4e7469982f8 32
# md5被撞库的概率较大，可以通过加盐来提高安全性
obj = md5(b'iamsalt')
name = "AliciaDragoon".encode('utf-8')
obj.update(name)
val = obj.hexdigest()
print(val, len(val))
# bca870b634aea83d0a9d981aee22b9fa 32
