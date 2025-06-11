from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Book(BaseModel):
    title: str 
    author: str
    year: str

d = {}  # Dictionary to store books, keyed by ID

@app.post("/review")
def review(rev: Book):
    global d
    id = len(d) + 1
    d[id] = rev
    return {id:rev}

@app.put("/review/{id}")
def updateById(id: int, rev: Book):
    global d
    if id not in d:
        raise HTTPException(status_code=404, detail="Book not found")
    d[id] = rev
    return rev

@app.get("/review/{id}",)
def getById(id: int):
    global d
    if id not in d:
        raise HTTPException(status_code=404, detail="Book not found")
    return d[id]

@app.get("/review")
def get_review():
    global d
    return {id: book.dict() for id, book in d.items()}  # Proper serialization

@app.delete("/review/{id}")
def deleteById(id: int):
    global d
    if id not in d:
        raise HTTPException(status_code=404, detail="Book not found")
    del d[id]
    return {}

@app.get("/")
def read_root():
    return {"message": "Welcome to the Book Review API!"}

