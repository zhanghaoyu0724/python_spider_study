from multiprocessing import Process, Queue
队列共享

# + 导入
#
#   from multiprocessing import Queue
#
# + 使用
#
#   que = Queue()  #创建队列
#
#   que.put(数据)  #压入数据
#
#   que.get()           #获取数据
#
# + 队列常用函数
#
#   Queue.empty() 如果队列为空，返回True, 反之False
#
#   Queue.full() 如果队列满了，返回True,反之False
#
#   Queue.get([block[, timeout]]) 获取队列，timeout等待时间
#
#   Queue.get_nowait() 相当Queue.get(False)
#
#   Queue.put(item) 阻塞式写入队列，timeout等待时间
#
#   Queue.put_nowait(item) 相当Queue.put(item, False)
#
# + 特点：先进先出
#
# + 注意：
#
#   get方法有两个参数，blocked和timeout，意思为阻塞和超时时间。默认blocked是true，即阻塞式。
#
#   当一个队列为空的时候如果再用get取则会阻塞，所以这时候就需要吧blocked设置为false，即非阻塞式，实际上它就会调用get_nowait()方法，此时还需要设置一个超时时间，在这么长的时间内还没有取到队列元素，那就抛出Queue.Empty异常。
#
#   当一个队列为满的时候如果再用put放则会阻塞，所以这时候就需要吧blocked设置为false，即非阻塞式，实际上它就会调用put_nowait()方法，此时还需要设置一个超时时间，在这么长的时间内还没有放进去元素，那就抛出Queue.Full异常。
#
#   另外队列中常用的方法
#
# + 队列的大小
#
#   Queue.qsize() 返回队列的大小 ，不过在 Mac OS 上没法运行。
#
# 实例
def run(queue):
    queue.put(['a','b','c'])

if __name__ == '__main__':
    queue = Queue()
    queue.put([1,2,3,4,5])
    p = Process(target=run, args=(queue,))
    p.start()
    p.join()
    print(queue.get())
    print(queue.get())