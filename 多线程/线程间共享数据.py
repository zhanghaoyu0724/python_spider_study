
import  threading
import  time

money=0
def run1():
    global money
    money =1
    print("run1 ------",money)
    print(f"启动子{threading.current_thread().name}线程")
    for i in range(10):
        print("luck is a good man")
        time.sleep(1)

    pass
def run2(name,word):
    print("run2----",money)

    for i in range(10):
        print("%s is a %s man"%(name,word))
        time.sleep(1)

if __name__ == '__main__':
    time1 = time.time()
    t1 = threading.Thread(target=run1,name = "name1")
    t2 = threading.Thread(target=run2,args=("name1","nice"))
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    time2 = time.time()
    print(f'{time2-time1} 时间消耗')
