from fastapi import FastAPI

app = FastAPI()

# main route
@app.get("/")
async def read_root():
    return {"Hello": "World"}
