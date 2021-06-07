from gevent import monkey; monkey.patch_all()
from gevent.lock import BoundedSemaphore
from gevent.pool import Pool
from requests import get
from urllib.request import *
import time


class Download:
    def __init__(self, url, file, nums=10):
        self.url = url
        self.num = nums
        self.name = file
        self.lock = BoundedSemaphore()
        req = Request(url=self.url, method='HEAD')
        req.add_header('Accept', '*/*')
        req.add_header('Charset', 'UTF-8')
        req.add_header('Connection', 'Keep-Alive')
        f = urlopen(req)
        # 获取要下载的文件的大小
        self.size = int(dict(f.headers).get('Content-Length', 0))
        f.close()
        self.count = 0
        print('该文件大小为：{} bytes'.format(self.size))

    def down(self, start, end):
        headers = {'Range': 'bytes={}-{}'.format(start, end)}
        # stream = True 下载的数据不会保存在内存中
        r = get(self.url, headers=headers, stream=True)
        # 写入文件对应位置,加入文件锁
        self.lock.acquire()
        with open(self.name, "rb+") as fp:
            fp.seek(start)
            fp.write(r.content)
        self.lock.release()
            # 释放锁

    def run(self):
        # 创建一个和要下载文件一样大小的文件
        fp = open(self.name, "wb")
        fp.truncate(self.size)
        fp.close()
        # 启动多线程写文件
        part = self.size // self.num
        pool = Pool(size=self.num)

        for i in range(self.num):
            start = part * i
            # 最后一块
            if i == self.num - 1:
                end = self.size
            else:
                end = start + part - 1
                print('{}->{}'.format(start, end))
            pool.spawn(self.down, start, end)
        pool.join()
        print('%s 下载完成' % self.name)


if __name__ == '__main__':
    start_time = time.time()
    download = Download(url='https://dl.softmgr.qq.com/original/Compression/7z1900-x64.exe', file='7z.exe')
    download.run()
    print('spend time:', time.time() - start_time)
