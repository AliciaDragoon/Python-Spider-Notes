# 与redis交互
# 查询
#    先给满分的，再给有分的，没有就不给了
# 新增
#    先判断是否存在该ip，如果存在就不执行新增操作
# ip改分
#    可用满分，不可用扣分
# 删除
from redis import Redis
import random
# from settings import REDIS_HOST, REDIS_PORT, REDIS_DB, REDIS_PASSWORD, REDIS_KEY
from settings import *


class ProxyRedis:
    # 链接保存在self.red里
    def __init__(self):
        self.red = Redis(
            host=REDIS_HOST,
            port=REDIS_PORT,
            db=REDIS_DB,
            password=REDIS_PASSWORD,
            decode_responses=True
        )

    # 判断IP是否存在
    def add_proxy_ip(self, ip):
        if not self.red.zscore(REDIS_KEY, ip):
            self.red.zadd(REDIS_KEY, {ip: DEFAULT_SCORE})
            print("采集到新的ip地址了", ip)
        else:
            print("ip地址已存在", ip)

    # 校验所有ip
    def get_all_proxy(self):
        return self.red.zrange(REDIS_KEY, 0, -1)

    # 可用满分
    def set_max_score(self, ip):
        self.red.zadd(REDIS_KEY, {ip: MAX_SCORE})

    # 不可用扣分
    def desc_incrby(self, ip):
        # 查询分值
        score = self.red.zscore(REDIS_KEY, ip)
        # 如果分值大于0就扣一分
        if score > MIN_SCORE:
            self.red.zincrby(REDIS_KEY, -1, ip)
        # 如果分值为0就删除
        else:
            self.red.zrem(REDIS_KEY, ip)

    def get_keyong_proxy(self):
        ips = self.red.zrangebyscore(REDIS_KEY, MAX_SCORE, MAX_SCORE, 0, -1)
        # 可能没有满分的ip
        if ips:
            # 从ips这个列表里随机抽一个返回
            return random.choice(ips)
        else:
            # 没有满分的就随机返回一个
            ips = self.red.zrangebyscore(REDIS_KEY, DEFAULT_SCORE + 1, MAX_SCORE - 1, 0, -1)
            if ips:
                return random.choice(ips)
            else:
                print("没有可用的ip")
                return None
