import pandas as pd
from pyscript import display
import json
import js
import matplotlib.pyplot as plt

#%matplotlib inline

with open('ingredients.json') as json_file:

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

#Create dict from json
    ingredient_list = json.load(json_file)

#Build dataframe from dict
    global df1
    df1 = df_recursive_create(ingredient_list["ingredients"])

#Plot a column of data
    #df1.plot.barh(x="name", y="calories_per_gram", figsize=(30, 5))
    #plt.show()


#Export to sessionStorage as a JSON
    jsonDf = df1.to_json()
    #js.sessionStorage.setItem("df", jsonDf)




#Create recipe dict from recipe JSON
#pseudocode:

with open('recipes.json') as json_file:

#Create dict from json
    global recipe_list
    recipe_list = json.load(json_file)
    js.sessionStorage.setItem("recipe_list", recipe_list)
    #display(print("recipe_list: ", recipe_list))
    #display(print("recipe list type: ", type(recipe_list["recipes"])))



def calc_tot_mass_per_ingred(list_of_recipes, ingredient_dataframe, monthly_caloric_limit=60000):

  #ser=pd.Series(range(len(ingredient_dataframe.index)))

  ingredient_dataframe['total_grams'] = pd.Series([0] * len(ingredient_dataframe))
  calories = 0
  i = 0
  while calories <= monthly_caloric_limit:
    if i == len(list_of_recipes):
      i = 0
    ingredient_list = list_of_recipes[i]["ingredients_and_amounts_in_milliliters"]
    recipe_name = list_of_recipes[i]["name"]
    #display(print("Recipe name: ", recipe_name))
    for j in range(0, len(ingredient_list) - 1, 2):
      ingredient_name = ingredient_list[j]
      #display(print("this is ingredient_name: ", ingredient_name))
      dataframe_label = ingredient_dataframe.index[ingredient_dataframe['name'] == ingredient_name][0]
      #display(print("this is dataframe_label: ", dataframe_label))
      ingredient_volume_in_ml = float(ingredient_list[j + 1])
      #display(print("this is ingredient volume in ml: ", type(ingredient_volume_in_ml)))
      ingredient_grams_per_milliliter = ingredient_dataframe.at[dataframe_label, "ingredient_grams_per_milliliter"]
      #display(print("this is ingredient grams per ml: ", type(ingredient_grams_per_milliliter)))
      #total_mass_of_ingredient = ingredient_dataframe.at[dataframe_label, "total_grams"]
      #display(print("this is total mass of ingred: ", total_mass_of_ingredient))

      mass_of_ingredient = ingredient_volume_in_ml * ingredient_grams_per_milliliter

      #display(print(ingredient_name, " mass equals: ", ingredient_volume_in_ml, "ml times ", ingredient_grams_per_milliliter, " g/ml equals ", mass_of_ingredient, " grams"))

      ingredient_dataframe.at[dataframe_label, "total_grams"] = ingredient_dataframe.at[dataframe_label, "total_grams"] + mass_of_ingredient

    calories = calories + list_of_recipes[i]["recipe_calories"]
    i = i + 1

  return ingredient_dataframe


df2 = calc_tot_mass_per_ingred(recipe_list["recipes"], df1)
display(df2)
display(print("the total mass of food for month is: ", df2['total_grams'].sum()))
df2.plot.barh(x="name", y="total_grams", figsize=(30, 5))
plt.show()

jsonDf2 = df2.to_json()
js.sessionStorage.setItem("df", jsonDf2)