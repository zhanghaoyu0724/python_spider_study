import  multiprocessing as mp


num_list= []
def fun():
    global num_list
    num_list.append(1)
    num_list.append(2)
    print(num_list)
if __name__ == '__main__':
    p = mp.Process(target=fun)
    p.start()
    p.join()
    print(num_list)
