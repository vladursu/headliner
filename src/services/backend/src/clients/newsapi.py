import httpx
from src.config import NEWSAPI_API_KEY
from src.dto.resources import HeadlineArticles

BASE_URL = "https://newsapi.org/v2/"
TOP_HEADLINES_ENDPOINT = "top-headlines"


async def get_top_headlines(
    country: str | None, category: str | None
) -> HeadlineArticles:
    country_parameter = f"&country={country}" if country else ""
    category_paramenter = f"&category={category}" if category else ""
    url = f"{BASE_URL}{TOP_HEADLINES_ENDPOINT}?apiKey={NEWSAPI_API_KEY}{country_parameter}{category_paramenter}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        return HeadlineArticles.model_validate(response.json())
