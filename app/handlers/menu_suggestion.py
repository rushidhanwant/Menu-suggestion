from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

from app.config import config

load_dotenv(config.env_path)


def scale_ingredients(ingredients: str, yields: str, servings: str ):
    # prompt template for scaling ingredients.
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
        Only provide the scaled ingredients as output and do not provide the steps.
    """

    result = ""

    try:
        prompt = ChatPromptTemplate.from_template(template)
        model = ChatOpenAI(model_name="gpt-3.5-turbo")
        chain = prompt | model
        result = chain.invoke({"ingredients": ingredients, "yields": yields, "servings": servings})
    except:
        result = "some error occurred"

    return result


def menu_suggestion(ingredients: str, servings: str):
    # prompt template for menu suggestion.
    template = f"""
        You are expert at suggesting recipe based on the ingredients provided to you.
        
        you will be given list of ingredients delimited by ``` and servings delimited by <>. Your job is to suggest the menu based on the ingredients 
        provided to you for given servings. Make sure that menu should contain at least 3 dishes and you have to provide instructions for each dish.
        
       output should be the below format.
       Recipe name 
       Ingredients List 
       Instructions
       
        ```{ingredients}```
        <{servings}>
        """

    result = ""

    try:
        prompt = ChatPromptTemplate.from_template(template)
        model = ChatOpenAI(model_name="gpt-3.5-turbo")
        chain = prompt | model
        result = chain.invoke({"ingredients": ingredients, "servings": servings})
    except:
        result = "some error occurred"

    return result


def suggest_menu(recipe):
    # scale_ingredients will first scale the ingredients based on the servings
    # once we get the scaled ingredients' menu_suggestion function will suggest menu based on the ingredients
    # provided to the function.

    scaled_version = scale_ingredients(recipe.ingredients, recipe.yields, recipe.servings)
    suggested_menu = menu_suggestion(scaled_version, recipe.servings)
    return {"scaled_recipe":scaled_version, "suggested_menu": suggested_menu}

