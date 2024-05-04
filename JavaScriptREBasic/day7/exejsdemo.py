# 在导入execjs之前，将popen的encoding锁定为utf—8，防止中文乱码问题
from functools import partial
import subprocess
subprocess.Popen = partial(subprocess.Popen, encoding='utf8')

import execjs

# print(execjs.get().name)

f = open("jsExample.js", mode="r", encoding="utf-8")
js = f.read()

# 加载js代码
obj = execjs.compile(js)

# 传递函数名和参数
# ret = obj.call("fn", 3, 5)
# print(ret)

ret = obj.call("gn")
print(ret)
