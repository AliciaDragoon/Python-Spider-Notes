# 用爬虫抓取采集代理ip
# test_url = "https://www.kuaidaili.com/free/dps/1/"
# redis查询效率最高，可使用集合去重，zset可有序存储查询
# ip{192.168.0.1:10, 192.168.0.2:100}
# 爬取的ip地址可用给100分，不可用给10分

# 验证ip的有效性
# 每轮验证时，ip可用给100分，不可用扣1分
# 分数扣完则表示不可用

# 提供免费的可用代理ip
# 需要ip时直接拿到最高分的ip即可

# 使用多进程，redis管理队列
