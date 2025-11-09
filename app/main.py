from fastapi import FastAPI

app = FastAPI()

# main
@app.get("/")
async def read_root():
    return {"Hello": "World"}
