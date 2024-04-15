from threading import Thread
from multiprocessing import Process
# Process()和Thread()的语法完全相同
from concurrent.futures import ProcessPoolExecutor
# 进程池的用法和线程池的也完全相同
# 创建线程的开销比进程低，需要多个独立的程序的时候再考虑多进程
