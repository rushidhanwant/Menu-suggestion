from recipe_scrapers import scrape_me


def scrape_recipe_handler(link: str):
    # scraper_me function will scrape the webpage
    # scraper.to_json() contains whole content in the json format
    data = {}
    scrapper = {}
    try:
        scraper = scrape_me(link, wild_mode=True)
    except Exception as e:
        return {"error": e, "message": "something went wrong"}

    return scraper.to_json()

