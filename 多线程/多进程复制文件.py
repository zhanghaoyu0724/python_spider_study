import time
from multiprocessing import Pool
import os

def copy_file(path, toPath):
    with open(path, "rb") as fp1:
        with open(toPath, "wb") as fp2:
            while 1:
                info = fp1.read(1024)
                if not info:
                    break
                else:
                    fp2.write(info)
                    fp2.flush()

if __name__ == "__main__":
    t1 = time.time()
    path = r"/Users/xialigang/Desktop/视频"
    dstPath = r"/Users/xialigang/Desktop/1视频"
    fileList = os.listdir(path)
    pool = Pool()

    for i in fileList:
        newPath1 = os.path.join(path, i)
        newPath2 = os.path.join(dstPath, i)
        pool.apply_async(copy_file, args=(newPath1, newPath2))

    pool.close()
    pool.join()

    t2 = time.time()
    print("耗时：%.2f"%(t2-t1))