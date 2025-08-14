from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from crawl import run_crawler

app = FastAPI()

class URLRequest(BaseModel):
    url: str

@app.post("/crawl")
async def create_crawl_job(request: URLRequest):
    try:
        result = await run_crawler(request.url)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def read_root():
    return {"status": "API is running"}
