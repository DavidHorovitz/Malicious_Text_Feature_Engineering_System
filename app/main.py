from fastapi import FastAPI

app = FastAPI()

@app.get("/GET")
async def get_data():
    return dl.get_all_data()


