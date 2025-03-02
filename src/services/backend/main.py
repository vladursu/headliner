from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from src.clients.newsapi import get_top_headlines
from src.agents.llm_agent import llama_agent
from src.agents.prompt_templates import (
    DATA_EXTRACTION_TEMPLATE,
    HEADLINES_RECOMMENDER_TEMPLATE,
)
from src.dto.resources import HeadlinesRequest, HeadlinesResponse, ExtractedData

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

# TODO:
# - add tests
# - add dockerfiles
# - add README


@app.post("/headlines", response_model=HeadlinesResponse)
async def main(request: HeadlinesRequest):
    HEADLINES_LIMIT = 30
    try:
        extracted_data = ExtractedData.model_validate_json(
            await llama_agent.get_completion(
                DATA_EXTRACTION_TEMPLATE.format(user_input=request.query)
            )
        )
    except:
        return HeadlinesResponse(
            response="Couldn't determine topic or location, please expand on your query."
        )

    headlines = await get_top_headlines(
        country=extracted_data.country, category=extracted_data.category
    )
    if not headlines.articles:
        return HeadlinesResponse(
            response="There are no headlines or your query is too restrictive, please expand on your query."
        )

    # Limit number of articles to avoid running out of context
    headlines.articles = headlines.articles[
        : min(HEADLINES_LIMIT, len(headlines.articles))
    ]

    return HeadlinesResponse(
        response=await llama_agent.get_completion(
            HEADLINES_RECOMMENDER_TEMPLATE.format(
                news_context=headlines.model_dump_json(), user_input=request.query
            )
        )
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=50051)
