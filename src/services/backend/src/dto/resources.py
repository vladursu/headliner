from typing import List, Optional
from pydantic import BaseModel


class HeadlinesRequest(BaseModel):
    query: str


class HeadlinesResponse(BaseModel):
    response: str


class ExtractedData(BaseModel):
    country: Optional[str] = None
    category: Optional[str] = None


class HeadlineArticle(BaseModel):
    author: str
    title: str
    description: str
    url: str


class HeadlineArticles(BaseModel):
    articles: List[HeadlineArticle]
