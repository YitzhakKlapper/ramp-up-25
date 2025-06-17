import os
import redis
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

channel = "channel1"
redis_host = os.getenv("REDIS_HOST", "localhost")
r = redis.Redis(host=redis_host, port=6379, db=0)

class Message(BaseModel):
    message: str

@app.post("/publish")
def publish(m: Message):
    r.publish(channel, m.message)
    return {"message": m.message}
