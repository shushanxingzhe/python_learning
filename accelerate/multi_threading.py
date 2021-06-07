from concurrent.futures import ThreadPoolExecutor, as_completed
import threading
import time
from datetime import datetime

'''
Suitable for parallel executing IO intensive tasks
'''


def worker(params):
    output = []
    for i in params:
        print(datetime.now(), threading.get_ident())
        output.append(i * 2)
        time.sleep(1)
    return output


pool = ThreadPoolExecutor(max_workers=10)
tasks = list(range(1, 300))
task_size = len(tasks)
batch_size = 30
futures = []
for i in range(0, task_size, batch_size):
    print(i, min(i+batch_size, task_size))
    batch = tasks[i:min(i+batch_size, task_size)]
    futures.append(pool.submit(worker, batch))

pool.shutdown(wait=True)
result = []
for future in as_completed(futures):
    items = future.result()
    result.extend(items)
print(result)
