
import  threading
import time


#Timer是Thread的子类，可以指定时间间隔后在执行某个操作



def go():
    print("揍我了")
    pass

if __name__ == '__main__':
    time1 = time.time()
    t = threading.Timer(2,go)
    t.start()
    t.join()
    time2 =time.time()

    print(f"耗时：{time2-time1}")