from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from src.clients.newsapi import get_top_headlines

app = FastAPI()

origins = [
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def main():
    return await get_top_headlines("us", "health")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=50051)
