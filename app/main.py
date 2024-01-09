from dotenv import load_dotenv
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware


from app.config import config
from app.handlers.menu_suggestion import suggest_menu
from app.handlers.scrape_recipe import scrape_recipe_handler
from app.schemas.request import ScrapeLink, RecipeData

load_dotenv(config.env_path)

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/scrape_recipe")
async def scrape_recipe_route(link: ScrapeLink):
    result = scrape_recipe_handler(link.link)
    return result

@app.post("/get_menu_suggestion")
async def get_menu_suggestion_route(recipe_data: RecipeData):
    return suggest_menu(recipe_data)

