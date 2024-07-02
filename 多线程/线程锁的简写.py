import threading

i = 0
lock = threading.Lock()
def sum1():
    global i
    with lock:
        for x in range(1000000):
            i += x
            i -= x
        print('sum1', i)

def sum2():
    global i
    with lock:
        for x in range(1000000):
            i += x
            i -= x
        print('sum2', i)

if __name__ == '__main__':
    thr1 = threading.Thread(target=sum1)
    thr2 = threading.Thread(target=sum2)
    thr1.start()
    thr2.start()
    thr1.join()
    thr2.join()
    print('over')