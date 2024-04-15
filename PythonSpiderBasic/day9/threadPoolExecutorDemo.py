from concurrent.futures import ThreadPoolExecutor


def get_one_page_info(year):
    pass


if __name__ == '__main__':
    with ThreadPoolExecutor(16) as t:  # 创建线程池，含16个线程
        t.submit(get_one_page_info, "线程1")  # 向提线程池提交任务, submit(任务，任务执行时需要的参数)
        t.submit(get_one_page_info, "线程2")
        pass
    # with语句方便结束后自动完成一些操作

with ThreadPoolExecutor(16) as t:
    for i in range(4):
        t.submit(get_one_page_info, f"线程{i}")
# 每次建立新线程池都会消耗资源，尽量少建立新的线程池

