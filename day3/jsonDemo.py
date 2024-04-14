import json

s = ""

dic = json.loads(s)
lst = dic['hero']
with open("hero.txt", mode="w", encoding="utf-8") as f:
    for item in lst:
        name = item['name']
        title = item['title']
        f.write(name)
        f.write("|")
        f.write(title)
        f.write("\n")
