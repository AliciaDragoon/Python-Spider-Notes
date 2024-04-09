# 配置文件
# redis主机ip地址
REDIS_HOST = "127.0.0.1"
# redis端口号
REDIS_PORT = 6379
# redis数据库编号
REDIS_DB = 1
# redis密码
REDIS_PASSWORD = ""
# 存储在redis中的代理ip的key
REDIS_KEY = "proxy_ip"
# 默认初始分数
DEFAULT_SCORE = 10
# 最高分数
MAX_SCORE = 100
# 最低分数
MIN_SCORE = 0

# ip检测并发量
SEM_COUNT = 30
# 第一次启动等待时间
START_VERIFY_WAIT_TIME = 10
# 校验休眠时间

# 采集等待时间
