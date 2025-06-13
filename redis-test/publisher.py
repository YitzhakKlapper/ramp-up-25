import redis
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

channel = "channel1"
r = redis.Redis(host='localhost', port=6379, db=0)

class Message(BaseModel):
    message: str

@app.post("/publish")
def publish(m: Message):
    r.publish(channel, m.message)
    return {"message": m.message}