from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

from app.config import config

load_dotenv(config.env_path)
print(config.env_path, "   ", config.root_dir)


def scale_ingredients(ingredients: str, yields: str, servings: str ):
    template = f"""
    You are expert at scaling ingredients provided to you .
    You will be provided with the ingredients yield for the recipe .
    your job is to scale the ingredients to the servings provided to you.
    
    for example if recipe is for 2 people and servings are 4 you will have to scale the recipe by 2.
    
    Below are the original ingredients provided to you which are for {yields} people
    
    {ingredients} 

    your job is to scale the ingredients by {servings} people 
    
    and provide the scaled ingredients as output. 
    
    NOTE- Make sure to check the original ingredients are for how many people and then only scale it to the provided number.
        Only provide the scaled ingredients as output.
    """

    prompt = ChatPromptTemplate.from_template(template)
    model = ChatOpenAI(model_name="gpt-3.5-turbo")
    chain = prompt | model
    result = chain.invoke({"ingredients": ingredients, "yields": yields, "servings": servings})
    return result

def menu_suggestion(ingredients):
    template = f"""
        You are expert at suggesting recipe based on the ingredients provided to you.
        
        you will be given list of ingredients delimited by ```. Your job is to suggest the menu based on the ingredients 
        provided to you. Make sure that menu should contain at least 3 dishes.
        
        ```{ingredients}```
        """
    prompt = ChatPromptTemplate.from_template(template)
    model = ChatOpenAI(model_name="gpt-3.5-turbo")
    chain = prompt | model
    result = chain.invoke({"ingredients": ingredients})
    return result


def suggest_menu(recipe):

    scaled_version = scale_ingredients(recipe.ingredients, recipe.yields, recipe.servings)
    suggested_menu = menu_suggestion(scaled_version)
    return suggested_menu

