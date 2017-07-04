import redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)
print(r.get('foo'))
r.set('foo', 'bar456',600)
print(r.get('foo'))

