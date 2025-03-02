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
    author: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    url: Optional[str] = None


class HeadlineArticles(BaseModel):
    articles: List[HeadlineArticle]
