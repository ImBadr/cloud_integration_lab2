from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World!"}

@app.get("/movies")
def root():
    return {"message": "Hello World!"}