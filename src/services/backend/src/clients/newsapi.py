import httpx
from typing import List
from src.config import NEWSAPI_API_KEY

BASE_URL = "https://newsapi.org/v2/"
TOP_HEADLINES_ENDPOINT = "top-headlines"


async def get_top_headlines(country: str | None, category: str | None) -> List:
    country_parameter = f"&country={country}" if country else ""
    category_paramenter = f"&category={category}" if country else ""
    url = f"{BASE_URL}{TOP_HEADLINES_ENDPOINT}?apiKey={NEWSAPI_API_KEY}{country_parameter}{category_paramenter}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        response_json = response.json()
        return response_json["articles"] if "articles" in response_json else []
