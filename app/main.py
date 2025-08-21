from fastapi import FastAPI
from  manager import Manager
import uvicorn
app = FastAPI()

@app.get("/")
async def get_data():
    manager=Manager()
    df = manager.manager()
    if "_id" in df.columns:
        df = df.drop(columns=["_id"])
    if "TweetID" in df.columns:
        df["TweetID"] = df["TweetID"].astype(int).astype(str)
    return manager.manager().to_dict(orient="records")


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000)


