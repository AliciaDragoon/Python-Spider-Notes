# jsonp通用解决方案
import re
import json

txt = 'jsonpUserLevel({"code":0,"data":{"level":"61","score":0},"msg":"Success"})'
obj = re.compile(r"\((?P<code>.*)\)")
r = obj.search(txt)
# print(r.group())
dic = json.loads(r.group("code"))
print(dic)
