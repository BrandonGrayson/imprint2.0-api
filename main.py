from fastapi import Body, FastAPI

app = FastAPI()

name = 'Brandon'

print(name)

@app.get("/")
async def root():
    return {"Greeting": name}

@app.post("/discover")
async def root(data: dict = Body(...)):
    print(data)
    return {"Discover": "new Music"}