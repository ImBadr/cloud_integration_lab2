import uvicorn
import time
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

URL= "http://localhost:8080/movies"

class Actor(BaseModel):
    firstname: str
    lastname: str

Denzel_Washington = Actor(firstname = "Denzel", lastname="Washington")
Idris_ELba = Actor(firstname = "Idris", lastname="Elba")
Will_Smith = Actor(firstname = "Will", lastname="Smith")
Tom_Hanks = Actor(firstname = "Tom", lastname="Hanks")
Al_Pacino = Actor(firstname = "Al", lastname="Pacino")
Tom_Cruise = Actor(firstname = "Tom", lastname="Cruise")
Bruce_Willis = Actor(firstname = "Bruce", lastname="Willis")
Dwayne_Johnson = Actor(firstname = "Dwayne", lastname="Johnson")

actors = {
    1: [Denzel_Washington, Idris_ELba],
    2: [Will_Smith, Tom_Hanks],
    3: [Al_Pacino, Tom_Cruise],
    4: [Bruce_Willis, Dwayne_Johnson]
}

@app.get("/movies/{id}/actors")
async def root(id: int):
    time.sleep(4)

    if not id:
        return actors

    if id not in actors.keys():
        return[]
    
    return actors[id]


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)