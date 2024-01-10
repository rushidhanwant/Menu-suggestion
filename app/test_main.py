import json

from fastapi.testclient import TestClient

from app.main import app
from app.mock_data import mock_suggestion_data

client = TestClient(app)


def test_invalid_input():
    response = client.post("/scrape_recipe", headers={"Content-Type": "application/json"}, data={"link": "abcd"})
    assert response.status_code == 422


def test_valid_input():
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


def test_get_scaled_menu():
    payload = {
        "servings": "9",
        "ingredients": [
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
        ],
        "instructions": "Pickle the carrots and/or cucumbers if desired (see recipe notes—I highly recommend).\nBrown\nIn a large skillet, brown the beef over medium-high heat, breaking it into small pieces, until it is browned and cooked through, about 5 or so minutes. When the beef is about halfway finished cooking, add 1 tablespoon of the soy sauce and 2/3 of the scallions. Once the beef is completely browned, stir in the garlic and cook 30 seconds.\nStir\nWhile the beef cooks, in a small bowl, stir together the rice vinegar, honey, ginger, red pepper flakes, and remaining soy sauce.\nPour over the browned beef. Stir and cook for 2 minutes. Remove from the heat, then stir in the sesame oil. Sprinkle the remaining green onion over the top. Taste and add extra soy sauce or red pepper flakes as desired (I added a bit more of each).\nServe the beef hot, over rice, topped generously with the carrots, cucumber, and sesame seeds.",
        "yields": "4"
    }
    response = client.post("/get_menu_suggestion", headers={"Content-Type": "application/json"},
                           data=json.dumps(payload))
    assert response.status_code == 200
    assert response.json()["scaled_recipe"]["content"] == mock_suggestion_data()["scaled_recipe"]["content"]


def test_get_menu_suggestion():
    payload = {
        "servings": "9",
        "ingredients": [
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
        ],
        "instructions": "Pickle the carrots and/or cucumbers if desired (see recipe notes—I highly recommend).\nBrown\nIn a large skillet, brown the beef over medium-high heat, breaking it into small pieces, until it is browned and cooked through, about 5 or so minutes. When the beef is about halfway finished cooking, add 1 tablespoon of the soy sauce and 2/3 of the scallions. Once the beef is completely browned, stir in the garlic and cook 30 seconds.\nStir\nWhile the beef cooks, in a small bowl, stir together the rice vinegar, honey, ginger, red pepper flakes, and remaining soy sauce.\nPour over the browned beef. Stir and cook for 2 minutes. Remove from the heat, then stir in the sesame oil. Sprinkle the remaining green onion over the top. Taste and add extra soy sauce or red pepper flakes as desired (I added a bit more of each).\nServe the beef hot, over rice, topped generously with the carrots, cucumber, and sesame seeds.",
        "yields": "4"
    }
    response = client.post("/get_menu_suggestion", headers={"Content-Type": "application/json"},
                           data=json.dumps(payload))
    assert response.status_code == 200
    assert response.json()["scaled_recipe"]["content"] == mock_suggestion_data()["suggested_menu"]["content"]
