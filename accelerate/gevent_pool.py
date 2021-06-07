from gevent import monkey; monkey.patch_all()
from gevent.pool import Pool
import time


def worker(k):
    time.sleep(1)
    print('worker %d ended' % k)


start_time = time.time()
pool = Pool(5)

for i in range(10):
    pool.spawn(worker, i)

pool.join()
print('spend time: ', time.time()-start_time)
