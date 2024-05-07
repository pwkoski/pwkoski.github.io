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