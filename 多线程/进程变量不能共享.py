import  multiprocessing as mp


num = 0
def fun():
    global num
    print(num)
    num+=1
    print(num)
if __name__ == '__main__':
    p = mp.Process(target=fun)
    p.start()
    p.join()
    print(num)
