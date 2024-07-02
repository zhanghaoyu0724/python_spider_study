import time
from concurrent.futures import ThreadPoolExecutor,as_completed

def go(str):
    print("thread hello :",str)
    time.sleep(2)
    return 'result:'+str
if __name__ == '__main__':
    pool = ThreadPoolExecutor(10)
    pool.submit(go)

    # 统一放入进程池使用

    # pool.map(go, [f'name{i}' for i in range(10)])

    # 多个参数
    # pool.map(go, name_list1, name_list2...)

    # for i in range(10):
    #     pool.submit(go,f'name{i}')

    # all_task =[pool.submit(go,f'name{i}') for i in range(10)]
    #
    # for tak in as_completed(all_task):
    #     print(tak.result())
    # print(all_task)


#方式二获取结果
    # for result in pool.map(go, [f'name{i}' for i in range(10)]):
    #     print("task:{}".format(result))

#方式三


from concurrent.futures import ThreadPoolExecutor, wait
import time

# 参数times用来模拟下载的时间
# def down_video(times):
#     time.sleep(times)
#     print("down video {}s finished".format(times))
#     return times
# executor = ThreadPoolExecutor(max_workers=2)
# #通过submit函数提交执行的函数到线程池中，submit函数立即返回，不阻塞
# task1 = executor.submit(down_video, (3))
# task2 = executor.submit(down_video, (1))
# # done方法用于判定某个任务是否完成
# print("任务1是否已经完成：", task1.done())
# time.sleep(4)
# print(wait([task1, task2]))
# print('wait')
# print("任务1是否已经完成：", task1.done())
# print("任务1是否已经完成：", task2.done())
# #result方法可以获取task的执行结果
# print(task1.result())