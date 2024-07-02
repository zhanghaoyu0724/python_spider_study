# import multiprocessing
# import time
# def fun():
#     time.sleep(100)
# if __name__=='__main__':
#     p = multiprocessing.Process(target=fun)
#     p.daemon = True
#     p.start()
#     print('over')

import multiprocessing
import time
def fun():
    time.sleep(100)
if __name__=='__main__':
    p = multiprocessing.Process(target=fun)
    p.start()
    p.terminate()
    p.join()
    print('over')