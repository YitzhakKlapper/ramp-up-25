import redis

channels = ["channel1"]

r = redis.Redis(host='localhost')
ps = r.pubsub()
for channel in channels:
    ps.subscribe(channel)

count = 1
for message in ps.listen():
    if message['type'] == 'message':
        print(f"message {count}: ",message['data'].decode('utf-8'))
        count += 1