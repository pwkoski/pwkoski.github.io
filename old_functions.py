#Recursive function that I built the recursive df create function

def recursive_items(dictionary):
    for key, value in dictionary.items():
        if type(value) is dict:
            yield from recursive_items(value)
        else:
            yield (key, value)

for key, value in recursive_items(dictionary):
    display(key, value)




#not really a function but this section of code will build the
#ingredient dataframe manually.  This may still be the primary way
#to build if the recursive version doesn't work.
#I: Depends on how you look at it, but either a json file, a dict, or, an array of dicts.
#O: A dataframe with all the ingredient data
#C: relies on knowing the column names first.

with open('ingredients.json') as json_file:
    #Create dict from json
    recipe_list = json.load(json_file)

    #Build dataframe manually from dict

    df2 = pd.DataFrame(columns=['Name',
                                "Growable?",
                                "Price Per Month ($)",
                                "Fresh?",
                                "Composite?",
                                "Ingredient Density (g/mL)",
                                "Grams Yield per Plant (g/plant)",
                                "Planting Density (plants/sq. m)",
                                "Amount per Container (g/container)",
                                "Storage Type",
                                "Container",
                                "Container Area Density (containers/sq. m)",
                                "Container Volume Density (containers/cu. m)",
                                "Protein %",
                                "Carb %",
                                "Fat %",
                                "Caloric Density (kcal/g)"
                                ])


    r = recipe_list["ingredients"]
    for i in range(len(r)):
       recipe = r[i]
       df2.loc[i] = [recipe["info"]["name"],
                     recipe["info"]["growable"],
                     recipe["info"]["price_per_month"],
                     recipe["info"]["fresh"],
                     recipe["info"]["composite"],
                     recipe["info"]["ingredient_grams_per_milliliter"],
                     recipe["growth"]["grams_yield_per_plant"],
                     recipe["growth"]["plants_per_square_meter"],
                     recipe["storage"]["grams_per_container"],
                     recipe["storage"]["storage_type"],
                     recipe["storage"]["storage"],
                     recipe["storage"]["containers_per_square_meter"],
                     recipe["storage"]["containers_per_cubic_meter"],
                     recipe["nutrition"]["protein_percentage"],
                     recipe["nutrition"]["carb_percentage"],
                     recipe["nutrition"]["fat_percentage"],
                     recipe["nutrition"]["calories_per_gram"]
                     ]







#generates a list of ingredients based on the recipe.json recipe list.
#I: recipe list, a dict with a single key (recipes) whose value is an array of recipes
#O: an array of strings, each string a unique ingredient in the recipes
#C: use the code below to generate an acceptable format to feed into function, which i think returns a dict from a json file.

#with open('recipes.json') as json_file:

# returns JSON object as
# a dictionary
#   recipe_list = json.load(json_file)

#Show result, can also use a print statement
   #display(generate_ingredient_list(recipe_list), append=True)

def generate_ingredient_list(recipe_list):
    ingredient_array = []
    for recipe in recipe_list["recipes"]:
        for i in range(0,len(recipe["ingredients_and_amounts_in_milliliters"]), 2):
            if recipe["ingredients_and_amounts_in_milliliters"][i] not in ingredient_array:
                ingredient_array.append(recipe["ingredients_and_amounts_in_milliliters"][i])
    return ingredient_array