import pandas as pd
from pyscript import display
import json


def generate_ingredient_list(recipe_list):
    ingredient_array = []
    for recipe in recipe_list["recipes"]:
        for i in range(0,len(recipe["ingredients_and_amounts_in_milliliters"]), 2):
            if recipe["ingredients_and_amounts_in_milliliters"][i] not in ingredient_array:
                ingredient_array.append(recipe["ingredients_and_amounts_in_milliliters"][i])
    return ingredient_array




with open('ingredients.json') as json_file:
    recipe_list = json.load(json_file)

    # Print the data of dictionary, change to "recipes.json"
    #display(generate_ingredient_list(recipe_list), append=True)

    # Print the ingredient list, change to "ingredients.json"
    display(recipe_list, append=True)


