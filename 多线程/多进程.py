import os
import time
from  multiprocessing import Process

def fun(name):
    print(f"我是{name}函数",'进程id:',os.getpid(),'进程父：',os.getppid())
    time.sleep(1)

if __name__ == '__main__':
    p =Process(target=fun,args=('zhanh',))
    p.start()
    p.join()
    print(os.getpid())
    print('lunck is a good time')