import redis

red = redis.Redis(
    host="127.0.0.1" ,
    port=6379,
    # password=,
    db=0,
    decode_responses=True
)

# red.set("Bob", "鲍勃")
# red.save()

# r = red.get("alex")
# print(r)

# red.hset("David", "name", "大卫")
# red.hset("David", "age", "20")
# red.save()

# r = red.hmget("David", "name", "age")
# print(r)

# r = red.hgetall("David")
# print(r)

# red.lpush("stu", "Alice", "Benjamin", "Catherine")
# r = red.lrange("stu", 0, -1)
# print(r)

# red.sadd("teac", "Emily", "Frank", "Grace")
# r = red.smembers("teac")
# print(r)

# red.zadd("score", {"Alice": 1, "Benjamin": 0,"Catherine": 6})
# r = red.zrange("score", 0, -1)
# print(r)

red.close()