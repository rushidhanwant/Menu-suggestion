import os

from dotenv import load_dotenv
from fastapi import FastAPI, Request, Security, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware

from app.config import config
from app.handlers.menu_suggestion import suggest_menu
from app.handlers.scrape_recipe import scrape_recipe_handler
from app.schemas.request import ScrapeLink, RecipeData

from fastapi.security import APIKeyHeader

from fastapi.security import HTTPBasic

from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi

security = HTTPBasic()

load_dotenv(config.env_path)

app = FastAPI(openapi_url="/api/openapi.json")

api_key_header = APIKeyHeader(name="x-api-key", auto_error=False)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api_keys = os.getenv("api_keys")


def get_api_key(api_key_header: str = Security(api_key_header)) -> str:
    if api_key_header == api_keys:
        return api_key_header
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or missing API Key",
    )

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/scrape_recipe")
async def scrape_recipe_route(link: ScrapeLink, api_key=Security(get_api_key)):
    result = scrape_recipe_handler(link.link)
    return result


@app.post("/get_menu_suggestion")
async def get_menu_suggestion_route(recipe_data: RecipeData, api_key=Security(get_api_key)):
    return suggest_menu(recipe_data)


@app.get("/docs", include_in_schema=False)
async def get_documentation(request: Request):
    root_path = request.scope.get("root_path", "").rstrip("/")
    openapi_url = root_path + app.openapi_url
    return get_swagger_ui_html(openapi_url=openapi_url, title="Swagger")


@app.get("/openapi.json", include_in_schema=False)
async def openapi():
    return get_openapi(title=app.title, version=app.version, routes=app.routes)