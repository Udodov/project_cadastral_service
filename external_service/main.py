from fastapi import FastAPI

app = FastAPI()


@app.get("/emulate")
async def emulate():
    return {"message": "This is a response from the emulated server"}
