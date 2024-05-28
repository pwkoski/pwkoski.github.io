import pandas as pd
from pyscript import document
import json
import js
import functions

with open('ingredients.json') as json_file:

#Create ingredient dict from json
    ingredient_list = json.load(json_file)

#Build dataframe from dict
    global df
    df = functions.df_recursive_create(ingredient_list["ingredients"])

#Create recipe dict from recipe JSON
with open('recipes.json') as json_file:

#Create dict from json and store in sessionStorage
    global recipe_list
    recipe_list = json.load(json_file)
    js.sessionStorage.setItem("recipe_list", recipe_list)

#Calculate the mass per month of ingredient and update dataframe
df = functions.calc_tot_mass_per_ingred(recipe_list["recipes"], df)

#Store the dataframe in sesssionStorage for other pages to use.
jsonDf = df.to_json()
js.sessionStorage.setItem("df", jsonDf)

#Display html table
df_display = df[['name', 'total_grams']]
df_display = df_display.rename(columns={'name': 'Ingredient Name', 'total_grams': 'Total Monthly Grams Consumed'})
df_html = df_display.to_html(index_names=False,index=False)
htmlObject = document.querySelector("#pythontable")
htmlObject.innerHTML = df_html