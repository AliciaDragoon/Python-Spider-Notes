import threading


def get_one_page_info(year):
    pass  # 该函数可参考day7/boxoffice2019SpyderDemo


if __name__ == '__main__':
    for y in range(1995, 2021):
        get_one_page_info(y)
        t1 = threading.Thread(target=get_one_page_info, args=(y,))  # Thread(任务，任务参数)
        t1.start()

# 创建线程也要消耗资源
# 多线程爬虫会给网站带来更大压力
# 建议创建cpu核心数2倍的线程
