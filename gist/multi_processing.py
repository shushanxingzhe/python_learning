from multiprocessing import Pool
import time
from datetime import datetime
import os

'''
Suitable for parallel executing computationally intensive tasks
'''


def worker(params):
    output = []
    for i in params:
        print(datetime.now(), os.getpid())
        output.append(i * 2)
        time.sleep(1)
    return output


if __name__ == '__main__':
    pool = Pool(10)
    tasks = list(range(1, 300))
    task_size = len(tasks)
    batch_size = 30
    futures = []
    for i in range(0, task_size, batch_size):
        print(i, min(i+batch_size, task_size))
        batch = tasks[i:min(i+batch_size, task_size)]
        futures.append(pool.apply_async(worker, args=(batch,)))

    pool.close()
    pool.join()
    result = []
    for future in futures:
        items = future.get()
        result.extend(items)
    print(result)
