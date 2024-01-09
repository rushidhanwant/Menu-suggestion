from pydantic import BaseModel, HttpUrl
from typing import List


class Req(BaseModel):
    query: str
    chat_history: List[dict] = []


class ScrapeLink(BaseModel):
    link: str


class RecipeData(BaseModel):
    servings: str
    ingredients: List[str]
    instructions: str
    yields: str
