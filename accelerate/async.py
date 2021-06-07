import aiohttp
import asyncio
from inspect import isfunction


def request(pool, data_list):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(exec(pool, data_list))


async def exec(pool, data_list):
    tasks = []
    sem = asyncio.Semaphore(pool)
    for item in data_list:
        tasks.append(
            control_sem(sem,
                        item.get("method", "GET"),
                        item.get("url"),
                        item.get("data"),
                        item.get("headers"),
                        item.get("callback")))
    await asyncio.wait(tasks)


async def control_sem(sem, method, url, data, headers, callback):
    async with sem:
        count = 0
        flag = False
        while not flag and count < 4:
            flag = await fetch(method, url, data, headers, callback)
            count = count + 1
            print("flag:{},count:{}".format(flag, count))
        if count == 4 and not flag:
            raise Exception('EAS service not responding after 4 times of retry.')


async def fetch(method, url, data, headers, callback):
    async with aiohttp.request(method, url=url, data=data, headers=headers) as resp:
        try:
            json = await resp.read()
            print(json)
            if resp.status != 200:
                return False
            if isfunction(callback):
                callback(json)
            return True
        except Exception as e:
            print(e)

def display(obj):
    print('result:',obj)

pool = 1
data_list = [{'url':'http://www.baidu.com/','data':None,'headers':None,'callback':display},{'url':'https://news.qq.com/','data':None,'headers':None,'callback':display}]
request(pool, data_list)


# import asyncio
#
#
# async def wget(host):
#     print('wget %s...' % host)
#     connect = asyncio.open_connection(host, 80)
#     reader, writer = await connect
#     header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
#     writer.write(header.encode('utf-8'))
#     await writer.drain()
#     while True:
#         line = await reader.readline()
#         if line == b'\r\n':
#             break
#         print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
#     # Ignore the body, close the socket
#     writer.close()
#
#
# loop = asyncio.get_event_loop()
# tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

