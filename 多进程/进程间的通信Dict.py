import  multiprocessing

def run(my_dict):
    my_dict['x']='x'
    my_dict['z']='z'
    my_dict['z']='z'

if __name__ == '__main__':
    my_dict =multiprocessing.Manager().dict()
    my_dict['x']='1'
    print(my_dict)
    p=multiprocessing.Process(target=run,args=(my_dict,))
    p.start()
    p.join()
    print(my_dict)