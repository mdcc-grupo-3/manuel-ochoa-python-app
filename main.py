from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/greet/{name}")
def read_item(name: str):
    return {"Greetings": name}
