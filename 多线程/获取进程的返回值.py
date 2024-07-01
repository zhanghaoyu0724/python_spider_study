from  multiprocessing import Pool


def run(args):
    print(args)
    return "done"
if __name__ == '__main__':
    pool =Pool(10)
    for i in range(10):
        result =pool.apply_async(run,args=({"name":"张浩宇"},))
        print(result.get())
    pool.close()
    pool.join()

    print("结束主线程")