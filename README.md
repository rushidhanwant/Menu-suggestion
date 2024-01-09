# eat-cook-joy-assignment

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

4. Run unit test

```bash
./script/test.sh
```

## Endpoints

```
1. "/scrape_recipe"    

Method- post
Input -  web link to the recipe 
Reponse -  scraped recipe from the web page.
                      
2. "/get_menu_suggestion" 

Method - post
Input - ingredeints, recipe instruction, yeild and servings  
Response - scaled ingredients and suggested menu by GPT

Api Documentation - http://domain/docs
```

