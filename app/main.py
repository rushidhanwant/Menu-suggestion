from dotenv import load_dotenv
from fastapi import FastAPI,Request
from fastapi.middleware.cors import CORSMiddleware


from app.config import config
from app.handlers.menu_suggestion import suggest_menu
from app.handlers.scrape_recipe import scrape_recipe_handler
from app.schemas.request import ScrapeLink, RecipeData

from fastapi.security import HTTPBasic

from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi

security = HTTPBasic()

load_dotenv(config.env_path)

app = FastAPI(openapi_url="/openapi.json")

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


@app.get("/docs", include_in_schema=False)
async def get_documentation(request: Request):
    root_path = request.scope.get("root_path", "").rstrip("/")
    openapi_url = root_path + app.openapi_url
    return get_swagger_ui_html(openapi_url=openapi_url, title="Swagger")


@app.get("/openapi.json", include_in_schema=False)
async def openapi():
    return get_openapi(title=app.title, version=app.version, routes=app.routes)