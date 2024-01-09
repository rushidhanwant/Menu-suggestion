from recipe_scrapers import scrape_me


def scrape_recipe_handler(link: str):
    data = {}
    scraper = scrape_me(link, wild_mode=True)
    data["ingredients"] = scraper.ingredients()
    data["instructions"] = scraper.instructions()
    return scraper.to_json()

