from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import json
from src.clients.newsapi import get_top_headlines
from src.agents.llm_agent import llama_agent
from src.agents.prompt_templates import (
    DATA_EXTRACTION_TEMPLATE,
    HEADLINES_RECOMMENDER_TEMPLATE,
)

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
    user_input = "Any tech news from the Unites States?"
    extracted_data = json.loads(
        await llama_agent.get_completion(
            DATA_EXTRACTION_TEMPLATE.format(user_input=user_input)
        )
    )
    headlines = await get_top_headlines(
        country=extracted_data["country"], category=extracted_data["category"]
    )
    return await llama_agent.get_completion(
        HEADLINES_RECOMMENDER_TEMPLATE.format(
            news_context=json.dumps(headlines), user_input=user_input
        )
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=50051)
