import os
import redis

channels = ["channel1"]

redis_host = os.getenv("REDIS_HOST", "localhost")
r = redis.Redis(host=redis_host, port=6379, db=0)

ps = r.pubsub()
for channel in channels:
    ps.subscribe(channel)

print("Subscriber started and listening...", flush=True)

count = 1
for message in ps.listen():
    if message['type'] == 'message':
        print(f"message {count}: ", message['data'].decode('utf-8'), flush=True)
        count += 1
