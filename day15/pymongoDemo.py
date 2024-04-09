import pymongo

# 创建连接
coon = pymongo.MongoClient(
    host="localhost",
    port=27017
)
# 选择数据库
db = coon['testDb']
# 插入数据
# db.stu.insert_one({"name": "alex"})
# db.stu.insert_many([{"name": "solar"}, {"name": "tory"}, {"name": "relay"}])
# 查询数据
result = db.stu.find({}, {"_id": 0, "name": 1})
# 不查询id，只查询name
for item in result:
    print(item)
