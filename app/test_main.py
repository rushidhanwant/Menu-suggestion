import json

from fastapi.testclient import TestClient

from app.handlers.menu_suggestion import suggest_menu
from app.handlers.scrape_recipe import scrape_recipe_handler
from app.main import app
from app.mock_data import mock_scraper, mock_suggestion, mock_suggestion_data

client = TestClient(app)


def test_read_item():
    response = client.post("/scrape_recipe", headers={"Content-Type": "application/json"}, data={"link": "abcd"})
    assert response.status_code == 422


def test_get_response():
    response = client.post("/scrape_recipe", headers={"Content-Type": "application/json"},
                           data=json.dumps({"link": "https://www.wellplated.com/korean-beef-bowl/"}))
    assert response.status_code == 200
    assert response.json()["author"] == "Erin Clarke"


def test_get_ingredients():
    response = client.post("/scrape_recipe", headers={"Content-Type": "application/json"},
                           data=json.dumps({"link": "https://www.wellplated.com/korean-beef-bowl/"}))
    assert response.status_code == 200
    assert response.json()["ingredients"] == [
        "1 pound lean ground beef ((I used 93% lean))",
        "3 tablespoons low sodium soy sauce (plus additional to taste, divided)",
        "1 1/4 cups minced scallions (both green and white parts (from about 1 small bundle), divided)",
        "1 tablespoon minced garlic (about 3 cloves)",
        "2 tablespoons rice vinegar",
        "2 tablespoons honey",
        "2 tablespoons minced or finely grated fresh ginger",
        "1/4 teaspoon red pepper flakes (plus additional to taste)",
        "1 tablespoon sesame oil (plus additional to tase)",
        "Cooked brown rice (quinoa, or cauliflower rice)",
        "1 1/2 cups shredded carrots (see recipe notes to pickle them for an upgrade)",
        "Thinly sliced seedless cucumbers (Persian-style or English/hot house)",
        "Toasted sesame seeds"
    ]

