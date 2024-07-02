import multiprocessing
def fun(List):
    # print(mylist)
    List.append('x')
    List.append('y')
    List.append('z')
if __name__=='__main__':
# Manager是一种较为高级的多进程通信方式，它能支持Python支持的的任何数据结构。
    List = multiprocessing.Manager().list()
    p = multiprocessing.Process(target=fun,args=(List,))
    p.start()
    p.join()
    print(List)