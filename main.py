import pandas as pd
from pyscript import display
import json
import os


#display(os.getcwd(), append=True)
#display(os.listdir(), append=True)

def generate_ingredient_list(recipe_list):
    ingredient_array = []
    for recipe in recipe_list["recipes"]:
        for i in range(0,len(recipe["ingredients_and_amounts_in_milliliters"]), 2):
            if recipe["ingredients_and_amounts_in_milliliters"][i] not in ingredient_array:
                ingredient_array.append(recipe["ingredients_and_amounts_in_milliliters"][i])
    return ingredient_array




with open('recipes.json') as json_file:
    recipe_list = json.load(json_file)

    # Print the type of data variable
    #display(type(data), append=True)

    # Print the data of dictionary
    display(generate_ingredient_list(recipe_list), append=True)


#recipe_dict = js.load('recipes.json')
#df = pd.read_json('recipes.json')

#display(df, append=True)
#display(recipe_dict, append=True)



