import  multiprocessing as mp

def run(i):
    print(i)

if __name__ == '__main__':
    print("启动主线程")
    print(f'CPU number: {str(mp.cpu_count() )}')
    pool = mp.Pool(2)
    for i in range(10):
        pool.apply_async(run,args=(i,))

    pool.close()
    pool.join()
    
    print("结束主线程")