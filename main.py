from fastapi import FastAPI

app = FastAPI()

name = 'Brandon'

print(name)

@app.get("/")
async def root():
    return {"Greeting": name}