import pandas as pd

def df_recursive_create(array_of_dicts):

    df = pd.DataFrame()

    def recursion(dictionary, index):
        for key in dictionary:
            if type(dictionary[key]) is dict:
                return recursion(dictionary[key], index)
            else:
                df.at[index, key] = dictionary[key]

    for i in range(0, len(array_of_dicts)):
        for dictionary in array_of_dicts[i]:
            recursion(array_of_dicts[i][dictionary], i)

    return df






def calc_tot_mass_per_ingred(list_of_recipes, ingredient_dataframe, monthly_caloric_limit=60000):

  ingredient_dataframe['total_grams'] = pd.Series([0] * len(ingredient_dataframe))
  calories = 0
  i = 0

  while calories <= monthly_caloric_limit:

    if i == len(list_of_recipes):
      i = 0

    ingredient_list = list_of_recipes[i]["ingredients_and_amounts_in_milliliters"]

    recipe_name = list_of_recipes[i]["name"]

    for j in range(0, len(ingredient_list) - 1, 2):

      ingredient_name = ingredient_list[j]

      dataframe_label = ingredient_dataframe.index[ingredient_dataframe['name'] == ingredient_name][0]

      ingredient_volume_in_ml = float(ingredient_list[j + 1])

      ingredient_grams_per_milliliter = ingredient_dataframe.at[dataframe_label, "ingredient_grams_per_milliliter"]

      mass_of_ingredient = ingredient_volume_in_ml * ingredient_grams_per_milliliter

      ingredient_dataframe.at[dataframe_label, "total_grams"] = ingredient_dataframe.at[dataframe_label, "total_grams"] + mass_of_ingredient

    calories = calories + list_of_recipes[i]["recipe_calories"]
    i = i + 1

  return ingredient_dataframe