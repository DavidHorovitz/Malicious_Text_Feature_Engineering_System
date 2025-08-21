from fastapi import FastAPI
from  manager import Manager
import uvicorn
app = FastAPI()

@app.get("/")
async def get_data():
    manager=Manager()
    return manager.manager().to_dict(orient="records")


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000)


