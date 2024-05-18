

##  Installation Steps

1. Clone the repository

```bash
git clone https://github.com/rushidhanwant/eat-cook-joy-assignment.git
```

2. Install Dependencies

```bash
pip install -r requirement.txt
```

3. Add environment variables

```bash
OPENAI_API_KEY = 
```

4. Run the app

```bash
./script/run.sh
```


## Endpoints

```
1. "/scrape_recipe"    

Method- post

Input -  web link to the recipe 

Schema - { "link": "string" }

Reponse -  scraped recipe from the web page.
```
```
2. "/get_menu_suggestion" 

Method - post

Input - ingredeints, recipe instruction, yeild and servings 

Schema - {
  "servings": "string",
  "ingredients": ["string"],
  "instructions": "string",
  "yields": "string"
} 

Response - scaled ingredients and suggested menu by GPT

```

### Directory structure

    .
    ├── app
    │   ├── handlers
    │   │   ├── menu_suggestion.py
    │   │   └── scrape_recipe.py
    │   ├── schemas
    │   │   └── request.py
    │   ├── config.py
    │   ├── main.py
    │   ├── mock_data.py
    │   ├── test_main.py
    │   └── Utils.py
    ├── scripts
    ├── requirement.txt
    ├── .env
    └── README.md
    
    1. main.py - The entry point for your FastAPI application. Contains the server setup and routes .
    2. haandlers - This folder contains handler files which basically contains buisness logic
    3. menu_suggestion.py - This handler files contains code for scalling ingredients, suggesting menu and GPT setup. 
                            Scalling ingredients and menu suggestion is done using gpt.
    4. scrape_recipe.py - This file involves code for scraping recipe using recipe_scrapers package.
    5. Schmas/request.py -  This file contain schemas or structures for handling incoming requests.
    6. config.py - This file holds configuration settings for the application.
    7. mock_data.py - This file contain mock data for testing purposes.\
    8. test_main.py -  This is a test file for testing the functionality of main.py.
    9. Utils.py - This file holds algorithm for scalling ingredients without GPT.
    10. scripts - Contains bash scripts to run the server and run tests
    11. requirement.txt - Contains dependencies 

## Scaling Ingredients Algorithm
```angular2html
    Utils.py file contains algorithm for scaling ingredients without using GPT.
    The scraping library 'recipe_scrapers' does not scrape values and text separately from ingredients data, So i had to extract 
    value and text from ingredients list. 
    There were many ways in which the ingredients were written. 

    Few cases are mentioned below :-
    1. <whole number> <text>
    2. <fraction> <text>
    3. <whole number> <fraction> <text>
    4. <text> <whole number> <text>
    5. <text> <fraction> <text>
    6. <text>
    and many more
    
    I have handled cases where there were mixed fractions, whole number, fractions at 
    the start of the text. 
    Handling each and every case was very time consuming and there could be more possibilities of way
    ingredients can be written.
    Hence i have implemented scaling ingredients part using GPT which covers most of the edge cases.
```

## API Documentation
The API documentation for the FastAPI services is automatically generated using Swagger UI. To access the API documentation, open your web browser and go to https://convai.lv.launchventures.co/api/docs after starting the FastAPI server.


